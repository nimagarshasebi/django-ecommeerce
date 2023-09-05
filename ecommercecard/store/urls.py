from django.urls import path
from .views import ProductListView,index,productdetail

urlpatterns = [
    path('product-category/<slug:slug>/',ProductListView.as_view(),name='product-category'),
    path('product/<slug:slug>/',productdetail,name='product-detail'),
    path('',index,name='home'),

    ]