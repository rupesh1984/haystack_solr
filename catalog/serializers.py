from rest_framework import serializers
from .models import Catalog

class CatalogSerialiser(serializers.HyperlinkedModelSerializer):
    #total_skus = serializers.SerializerMethodField()

    class Meta:
        model = Catalog
        fields =('id', 'title', 'description', 'sku', 'price', 'image', 'created_at')

   # def get_price_with_currency(self, obj):
        

