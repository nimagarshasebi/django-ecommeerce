from .models import Category
from .models import Order
from users.models import Address
from users.forms import AddressForm

def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}
def addresses_processor(request):
    addresses = Address.objects.filter(customer=request.user)
    return {'addresses': addresses}
