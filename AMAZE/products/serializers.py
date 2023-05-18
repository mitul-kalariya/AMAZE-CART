from .models import Products
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import ProductsDocument


class ProductsDocumentSerializer(DocumentSerializer):
    class Meta:
        model = Products
        document = ProductsDocument
        size = 10000
        fields = "__all__"

        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}

        def get(self, obj):
            pass
