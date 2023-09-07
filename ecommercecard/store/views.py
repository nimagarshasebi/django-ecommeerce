import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category,Slider,Banner,BannerMobile
from django.db.models import Q
from django.http import JsonResponse
import json
from cart.forms import CartAddProductForm
from cart.cart import Cart

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)

# Create your views here.

class ProductListView(ListView):
     model = Product
     paginate_by =6
     context_object_name = 'products'
     template_name = 'store/product_list.html'
     def get_context_data(self, **kwargs):
         context = super(ProductListView, self).get_context_data(**kwargs)
         context['categories'] = Category.objects.all()
         return context
     def get_queryset(self):
         category_slug = get_object_or_404(Category, slug=self.kwargs.get('slug'))
         return Product.objects.filter(category=category_slug)



def productdetail(request,slug):

    product=get_object_or_404(Product,slug=slug)
    cart_add_product_form=CartAddProductForm()
    context = {'product': product,'cart_add_product_form':cart_add_product_form}
    return render(request,'store/product_detail.html',context)


# class ProductDetailView(DetailView):
#     model = Product
#     context_object_name = 'product'
#     template_name = 'store/product_detail.html'
#




def index(request):
    newproducts=Product.objects.filter(newproduct=True)
    bestsells=Product.objects.filter(bestsell=True)
    slideshowimg=Slider.objects.all()
    banner = Banner.objects.all()
    mobilebanner = Banner.objects.all()
    context={'newproducts':newproducts,'bestsells':bestsells,'slideshowimg':slideshowimg,'banner':banner,'mobilebanner':mobilebanner}
    return  render(request,'store/index.html',context)
@login_required()
def checkout(request):
    cart=Cart(request)
    return render(request,'store/checkout.html',{'cart':cart})