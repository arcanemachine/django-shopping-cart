from rest_framework import serializers

from stores.models import Store, Category, Item

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'registrant']
        read_only_fields = ['registrant']

    def create(self, validated_data):
        registrant = self.context['request'].user # make this in view
        store = Store.objects.create(registrant=registrant, **validated_data)
        return store


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'store', 'name', 'description']
        read_only_fields = ['store']

    def __init__(self, *args, **kwargs):
        if 'context' in kwargs \
                and kwargs['context'].get('store_pk', None):
            self.store = \
                Store.objects.get(pk=kwargs['context']['store'])
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        category = Category.objects.create(store=self.store, **validated_data)
        return menu


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'category', 'name', 'description', 'price']
        read_only_fields = ['category']

    def __init__(self, *args, **kwargs):
        if 'context' in kwargs and kwargs['context'].get('category_pk'):
            self.category = \
                Category.objects.get(pk=kwargs['context']['category'])
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        item = Item.objects.create(category=self.category, **validated_data)
        return menu

