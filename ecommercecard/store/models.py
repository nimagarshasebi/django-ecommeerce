from django.db import models
from django.urls import reverse
from users.models import Address
from django.db.models.signals import post_save
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
class Comment(models.Model):
    text=models.TextField(blank=False,max_length=750)
    name=models.CharField(blank=False,max_length=50)
    email=models.CharField(blank=False,max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',related_query_name='comment',null=True)
    comment_date=models.DateField(auto_now=True)
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
    order_date=models.DateTimeField(auto_now_add=True)
    order_address = models.ForeignKey('users.Address', on_delete=models.CASCADE,null=True)
    
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
class Invoice(models.Model):
    order=models.ForeignKey('Order',null=True,on_delete=models.SET_NULL)
    invoice_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.id}'
class Transaction(models.Model):
    STATUS_CHOICES={
        ('pending','Pending'),
        ('failed','Failed'),
        ('completed','Completed')
    }
    invoice=models.ForeignKey('Invoice',null=True,on_delete=models.SET_NULL)
    transactiondate=models.DateTimeField(auto_now_add=True)
    amount=models.DecimalField(max_digits=10,decimal_places=0)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    def __str__(self):
        return f'{self.id}'

