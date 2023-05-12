import time
from django.shortcuts import render
from django.views.generic import ListView,View
from products.models import Products
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
# Create your views here.

# class home_view(ListView):
#     model = 
#     def ():

class home_view(LoginRequiredMixin,ListView):
    model = Products
    template_name = 'Product/home.html'
    context_object_name = "products"
    paginate_by = 12


class search_view(LoginRequiredMixin,ListView):
    model = Products
    template_name = 'Product/search.html'
    context_object_name = "products"
    paginate_by = 12


    def post(self,request):
        self.object_list = self.get_queryset()
        return render(request,'Product/search.html',{'products':self.object_list})
    
    def get_queryset(self):
        qs = Products.objects.all()
        if self.request.POST:
            query = self.request.POST.get('query')
            # qs = Products.objects.annotate(rank=SearchRank(SearchVector('name'), SearchQuery(query))).order_by('-rank')
            start_time = time.perf_counter()
            qs =  Products.objects.annotate(search=SearchVector('name','main_category','sub_category' ),).filter(search=SearchQuery(query))
            data = {"queryset":qs,"time":str(time.perf_counter()-start_time), "query":query }
            return data
        else:
            return []