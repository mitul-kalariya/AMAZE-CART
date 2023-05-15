from django_elasticsearch_dsl import Document, fields, Index
from .models import Products


PRODUCTS_INDEX = Index("products_index_elastic")
PRODUCTS_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1,
)


@PRODUCTS_INDEX.doc_type
class ProductsDocument(Document):
    id = fields.IntegerField(attr="id")
    name = fields.TextField(fields={"raw": {"type": "keyword"}})
    main_category = fields.TextField(fields={"raw": {"type": "keyword"}})
    sub_category = fields.TextField(fields={"raw": {"type": "keyword"}})
    image = fields.TextField(fields={"raw": {"type": "keyword"}})
    link = fields.TextField(fields={"raw": {"type": "keyword"}})
    ratings = fields.TextField(fields={"raw": {"type": "keyword"}})
    no_of_ratings = fields.TextField(fields={"raw": {"type": "keyword"}})
    discount_price = fields.TextField(fields={"raw": {"type": "keyword"}})
    actual_price = fields.TextField(fields={"raw": {"type": "keyword"}})

    class Django(object):
        model = Products