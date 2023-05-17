from .models import Products
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *

class ProductsDocumentSerializer(DocumentSerializer):
    class Meta:
        model = Products
        document = ProductsDocument

        fields = ('id','name','main_category','sub_category','image','link','ratings','no_of_ratings','discount_price','actual_price')

        
        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}
        
        def get(self,obj):
            pass
