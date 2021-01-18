from rest_framework import serializers

from stores.models import Store, Category, Item

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ['id', 'name', 'registrant', 'image']
        read_only_fields = ['registrant']

    def create(self, validated_data):
        registrant = self.context['request'].user
        image = self.context['request'].data['file']
        store = Store.objects.create(
            registrant=registrant, image=image, **validated_data)
        return store


class CategorySerializer(serializers.ModelSerializer):
    store_name = serializers.CharField(max_length=128, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'store', 'store_name', 'name', 'description']
        read_only_fields = ['store_name', 'store']

    def __init__(self, *args, **kwargs):
        if 'context' in kwargs and kwargs['context'].get('store_pk'):
            self.store = Store.objects.get(pk=kwargs['context']['store_pk'])
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        category = Category.objects.create(store=self.store, **validated_data)
        return category

    def to_representation(self, instance):
        return {'id': instance.id,
                'name': instance.name,
                'description': instance.description,
                'store_name': instance.store.name,
                'store': instance.store.pk}


class ItemSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(initial=0, allow_null=True)

    class Meta:
        model = Item
        fields = ['id', 'category', 'name', 'description', 'price']
        read_only_fields = ['category']

    def __init__(self, *args, **kwargs):
        if 'context' in kwargs and kwargs['context'].get('category_pk'):
            self.category = \
                Category.objects.get(pk=kwargs['context']['category_pk'])
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        item = Item.objects.create(category=self.category, **validated_data)
        return item

    def to_representation(self, instance):
        return {'id': instance.id,
                'name': instance.name,
                'description': instance.description,
                'price': instance.price,
                'category_name': instance.category.name,
                'category': instance.category.pk,
                'store_name': instance.category.store.name,
                'store': instance.category.store.pk}
