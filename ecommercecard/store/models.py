from django.db import models
from django.urls import reverse
from users.models import Address
from django.db.models.signals import post_save
from django_jalali.db import models as jmodels
class Category(models.Model):
    name=models.CharField(blank=False,max_length=150)
    slug=models.SlugField(blank=False,max_length=50,default=1)
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    category=models.ManyToManyField(Category)
    slug=models.CharField(blank=False,max_length=50,default='youtube')
    title=models.CharField(blank=False,max_length=150)
    description=models.TextField(blank=False,max_length=750)
    product_image=models.ImageField(upload_to='uploads/products/')
    price=models.CharField(blank=True,max_length=20)
    discount=models.CharField(blank=True,max_length=20)
    newproduct=models.BooleanField(default=False)
    bestsell=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    def comment_counter(self):
        return Comment.objects.filter(product=self).count()
class Comment(models.Model):
    text=models.TextField(blank=False,max_length=750)
    name=models.CharField(blank=False,max_length=50)
    email=models.CharField(blank=False,max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',related_query_name='comment',null=True)
    comment_date=jmodels.jDateField(auto_now=True)
    def __str__(self):
        return f'{self.text}'

class Slider(models.Model):
    slideshow_image = models.ImageField(upload_to='uploads/slideshow/')

class Banner(models.Model):
    banner_image = models.ImageField(upload_to='uploads/banners/')

class BannerMobile(models.Model):
    banner_image = models.ImageField(upload_to='uploads/mobilebanners/')


class Order(models.Model):
    customer=models.ForeignKey('users.User',on_delete=models.CASCADE)
    order_date=jmodels.jDateTimeField(auto_now_add=True)
    order_address = models.ForeignKey('users.Address', on_delete=models.CASCADE,null=True)


    def get_total_price(self):
        total_price=0
        items=OrderItem.objects.filter(order=self)
        for item in items:
            total_price=total_price+item.product_cost
        return total_price


    def __str__(self):
        return f'{self.id}'
class OrderItem(models.Model):
    order=models.ForeignKey('Order',on_delete=models.CASCADE)
    product=models.ForeignKey('Product',null=True,on_delete=models.SET_NULL)
    product_price=models.DecimalField(max_digits=10,decimal_places=0)
    product_count=models.PositiveIntegerField()
    product_cost=models.DecimalField(max_digits=10,decimal_places=0)
    def __str__(self):
        return f'{self.id}'

class Transaction(models.Model):
    pending='درحال پردازش'
    failed='لغو'
    completed='ارسال شده'
    STATUS_CHOICES={
        (pending,'pending!'),
        (failed,'failed'),
        (completed,'completed')
    }
    order=models.ForeignKey('Order',null=True,on_delete=models.SET_NULL)
    transactiondate=jmodels.jDateTimeField(auto_now_add=True,)
    amount=models.DecimalField(max_digits=10,decimal_places=0)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default=pending)
    customer=models.ForeignKey('users.User',null=True,on_delete=models.SET_NULL)


    def __str__(self):
        return f'{self.id}'

