from django.urls import path
from .views import ProductListView,index,productdetail,checkout,search

urlpatterns = [
    path('product-category/<slug:slug>/',ProductListView.as_view(),name='product-category'),
    path('product/<slug:slug>/',productdetail,name='product-detail'),
    path('checkout/',checkout,name='checkout'),
    path('',index,name='home'),
    path('search/',search,name='search'),

    ]