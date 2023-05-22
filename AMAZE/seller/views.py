from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import SellerProfileForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SellerProfile,Seller
from authenticate.models import User
# Create your views here.


class BecomeASeller(View):
    # form_class = SellerProfileForm
    def get(self, request):
        form = SellerProfileForm
        return render(
            request,
            "Seller/profile_registration.html",{'form':form}
        )

    def post(self, request):
        form = SellerProfileForm(request.POST)
        breakpoint()
        if form.is_valid():
            updated_form = form.save(commit=False)
            updated_form.user = request.user
            updated_form.save()
            return redirect("")


def check_isseller(self):
    pass

class SellerHomepage(View):
    pass


@receiver(post_save,sender=SellerProfile)
def set_seller_true(sender, instance, created, **kwargs):
    if not created:
        user = instance.user
        user.is_seller = True
        print("user is set to seller true")
        user.save()
