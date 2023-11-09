from django.urls import path
from .views import ProductListView,index,productdetail,checkout,search,account_order,orderitem,cart_add_index,cart_add_category

urlpatterns = [
    path('product-category/<slug:slug>/',ProductListView.as_view(),name='product-category'),
    path('product/<slug:slug>/',productdetail,name='product-detail'),
    path('checkout/',checkout,name='checkout'),
    path('',index,name='home'),
    path('search/',search,name='search'),
    path('account-order/',account_order,name='account-order'),
    path('orderitem/<int:order_id>/',orderitem,name='orderitem'),
    path('add/<int:product_id>/',cart_add_index,name='cart-add-index'),
    path('add-item/<int:product_id>/',cart_add_category,name='cart-add-category'),


    ]