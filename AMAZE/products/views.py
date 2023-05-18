import time
from elasticsearch import Elasticsearch
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from products.models import Products
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import ProductsDocument
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
)
from .documents import ProductsDocument
from elasticsearch_dsl import Q
from rest_framework.generics import ListAPIView
from .serializers import ProductsDocumentSerializer
from rest_framework.pagination import PageNumberPagination



class home_view(LoginRequiredMixin, ListView):
    model = Products
    template_name = "Product/home.html"
    context_object_name = "products"
    paginate_by = 12


class search_view(LoginRequiredMixin, ListView):
    model = Products
    template_name = "Product/search.html"
    context_object_name = "products"
    paginate_by = 12

    def post(self, request):
        self.object_list = self.get_queryset()
        return render(request, "Product/search.html", {"products": self.object_list})

    def get_queryset(self):
        qs = Products.objects.all()
        if self.request.POST:
            query = self.request.POST.get("query")
            # qs = Products.objects.annotate(rank=SearchRank(SearchVector('name'), SearchQuery(query))).order_by('-rank')
            start_time = time.time()
            qs = Products.objects.annotate(
                search=SearchVector(
                    "name",
                    # 'main_category',
                    # 'sub_category'
                ),
            ).filter(search=SearchQuery(query))
            data = {
                "queryset": qs,
                "time":str( time.time() - start_time),
                "query": query,
                "no_of_results": len(qs),
            }
            return data
        else:
            return []


class search_elk_view(LoginRequiredMixin, ListView):
    template_name = "Product/search_elk.html"
    context_object_name = "products"
    paginate_by = 12

    def post(self, request):
        self.object_list = self.get_queryset()
        return render(request, "Product/search.html", {"products": self.object_list})

    def get_queryset(self):
        if self.request.POST:
            query_str = self.request.POST.get("query")
            search_query = Q("match_all")
            start_time = time.time()
            es_ans = list(search_for_questions(query_str))
            data = {
                "queryset": es_ans,
                "time": str( time.time() - start_time),
                "query": query_str,
                "no_of_results": len(es_ans),
            }
            return data
        else:
            return []


# class ProductsDocumentView(DocumentViewSet):
#     document = ProductsDocument
#     serializer_class = ProductsDocumentSerializer
#     filter_backends = [
#         FilteringFilterBackend,
#         CompoundSearchFilterBackend,
#     ]
#     pagination_class = None
#     search_fields = ("title", "main_category", "sub_category")
#     multi_match_search_fields = ("title", "main_category", "sub_category")
#     filter_fields = {
#         "title": "title",
#         "main_category": "main_category",
#         "sub_category": "sub_category",
#     }


# class ProductRESTDocumentView(DocumentViewSet):
#     # # serializer_class = ProductsDocumentSerializer
#     # queryset = Products.objects.all()
#     document = ProductsDocument
#     serializer_class = ProductsDocumentSerializer
#     filter_backends = [
#         FilteringFilterBackend,
#         CompoundSearchFilterBackend,
#     ]
#     pagination_class = PageNumberPagination


def search_for_questions(query):
    client =  Elasticsearch(["http://localhost:9200"], http_auth=("elastic", "root"))
    result = client.search(
        index="products_index_elastic",
        body={
            "size": 10000,
            "query": {
                "match": {
                    "name": query,
                },
            },
        },
    )
    return (h["_source"] for h in result["hits"]["hits"])
