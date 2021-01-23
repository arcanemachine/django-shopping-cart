from django.contrib.auth import get_user_model
from rest_framework import serializers

from django_shopping_cart.server_config import SERVER_LOCATION
from stores.models import Store, Category, Item
from users.models import Profile

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username']
        read_only_fields = ['username']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['cart']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'description', 'registrant', 'image']
        read_only_fields = ['registrant']

    def create(self, validated_data):
        registrant = self.context['request'].user
        image = self.context['request'].data['file']
        store = Store.objects.create(
            registrant=registrant, image=image, **validated_data)
        return store


class CategorySerializer(serializers.ModelSerializer):
    store_name = serializers.CharField(max_length=128, read_only=True)
    store_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = \
            ['id', 'name', 'description', 'image', 'store_name', 'store_id']
        read_only_fields = ['store_name', 'store_id']

    def __init__(self, *args, **kwargs):
        if 'context' in kwargs and kwargs['context'].get('store_pk'):
            self.store = Store.objects.get(pk=kwargs['context']['store_pk'])
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        category = Category.objects.create(store=self.store, **validated_data)
        return category

    def to_representation(self, instance):
        image_repr = \
            SERVER_LOCATION + instance.image.url if instance.image else None
        return {'id': instance.id,
                'name': instance.name,
                'description': instance.description,
                'image': image_repr,
                'store_name': instance.store.name,
                'store_id': instance.store.id}


class ItemSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(initial=0, allow_null=True)

    category_name = serializers.CharField(max_length=128, read_only=True)
    category_id = serializers.IntegerField(read_only=True)
    store_name = serializers.CharField(max_length=128, read_only=True)
    store_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'image',
                  'category_name', 'category_id', 'store_name', 'store_id']
        read_only_fields = \
            ['category_name', 'category_id', 'store_name', 'store_id']

    def __init__(self, *args, **kwargs):
        if 'context' in kwargs and kwargs['context'].get('category_pk'):
            self.category = \
                Category.objects.get(pk=kwargs['context']['category_pk'])
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        item = Item.objects.create(category=self.category, **validated_data)
        return item

    def to_representation(self, instance):
        image_repr = \
            SERVER_LOCATION + instance.image.url if instance.image else None
        return {'id': instance.id,
                'name': instance.name,
                'description': instance.description,
                'price': instance.price,
                'image': image_repr,
                'category_name': instance.category.name,
                'category_id': instance.category.id,
                'store_name': instance.category.store.name,
                'store_id': instance.category.store.id}
