from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SellerProfileForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SellerProfile, Seller
from authenticate.models import User
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# Create your views here.


class BecomeASeller(LoginRequiredMixin, View):
    # form_class = SellerProfileForm
    def get(self, request):
        form = SellerProfileForm
        return render(request, "Seller/profile_registration.html", {"form": form})

    def post(self, request):
        form = SellerProfileForm(request.POST)
        breakpoint()
        if form.is_valid():
            updated_form = form.save(commit=False)
            updated_form.user = request.user
            updated_form.save()
            return redirect("")


class SellerHomepage(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_seller

    def handle_no_permission(self) -> HttpResponseRedirect:
        user_with_profile_request = SellerProfile.objects.filter(
            user=self.request.user, is_active=False
        ).first()
        breakpoint()
        if user_with_profile_request:
            return HttpResponse("Your profile is under check")
        elif self.request.user.is_superuser:
            return HttpResponse("You are admin")
        else:
            return redirect("seller:be_a_seller")

    def get(self, request):
        return HttpResponse("Welcome aboard Seller")


@receiver(post_save, sender=SellerProfile)
def set_seller_true(sender, instance, created, **kwargs):
    if not created:
        user = instance.user
        user.is_seller = True
        print("user is set to seller true")
        user.save()
  