import datetime

from _decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category,Slider,Banner,BannerMobile,Order,OrderItem,Comment
from django.db.models import Q
from django.http import JsonResponse
import json
from cart.forms import CartAddProductForm
from cart.cart import Cart

from .forms import CommentForm
from users.models import User,Address

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
    product = get_object_or_404(Product, slug=slug)
    cart_add_product_form = CartAddProductForm()
    comments=Comment.objects.filter(product=product)



    if request.method=='POST':
        commentform=CommentForm(request.POST)
        if commentform.is_valid():

            new_comment=commentform.save(commit=False)
            new_comment.product=product
            new_comment.save()

    else:
        if request.user.is_authenticated:
            initial_data={'name':request.user.first_name,'email':request.user.email}
            commentform = CommentForm(initial=initial_data)
        else:
            commentform = CommentForm()

    context = {'product': product,'cart_add_product_form':cart_add_product_form,'commentform':commentform,'comments':comments}
    return render(request,'store/product_detail.html',context)

def index(request):
    slideshowimg=Slider.objects.all()
    banner = Banner.objects.all()
    mobilebanner = Banner.objects.all()
    newproducts = Product.objects.filter(newproduct=True)
    bestsells = Product.objects.filter(bestsell=True)
    context={'newproducts':newproducts,'bestsells':bestsells,'slideshowimg':slideshowimg,'banner':banner,'mobilebanner':mobilebanner}
    return render(request,'store/index.html',context)


@login_required
def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
            customer = request.user
            receiver_address=Address.objects.get(customer=customer,default_address=True)
            order = Order.objects.create(customer=customer,order_address=receiver_address)
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         product_price=item['price'],
                                         product_count=item['product_count'],
                                         product_cost=Decimal(item['product_count']) * Decimal(item['price']))

            cart.clear()


    return render(request, 'store/checkout.html', {'cart': cart})

def search(request):
    query = request.GET.get('search')
    if query:
        searchproduct= Product.objects.filter(title=query)
    return render(request,'store/search_result.html',{'searchproduct':searchproduct})