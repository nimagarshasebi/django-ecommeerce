from django.contrib.auth.decorators import login_required

from .models import Category
from .models import Order
from users.models import Address
from users.forms import AddressForm
from .forms import CartAddProductFormStore

def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}


def cartadd_processor(request):
    cart_add_form = CartAddProductFormStore()
    return {'cart_add':cart_add_form}




