from django.contrib import admin
from .models import Product,Category,Slider,Banner,BannerMobile,Order,OrderItem,Invoice,Transaction,Comment
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_date', 'order_address','customer')
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Banner)
admin.site.register(BannerMobile)

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Invoice)
admin.site.register(Transaction)
admin.site.register(Comment)





