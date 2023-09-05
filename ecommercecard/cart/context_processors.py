from .cart import Cart
def cart_processor(request):
    return {'cart':Cart(request)}