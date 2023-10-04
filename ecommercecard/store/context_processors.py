from django.contrib.auth.decorators import login_required

from .models import Category
from .models import Order
from users.models import Address
from users.forms import AddressForm

def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}

# def addresses_processor(request):
#         address = Address.objects.get(customer=request.user,default_address=True)
#         return {'address': address}


