from typing import Any, Optional
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomeView(TemplateView):
    template_name = "Home/homepage.html"


# @method_decorator(login_required(login_url="login"), name="dispatch")
class PreSellerRequestView(LoginRequiredMixin, RedirectView):
    pattern_name = "seller:be_a_seller"

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        return super().get_redirect_url(*args, **kwargs)


class SearchView(TemplateView):
    pass
