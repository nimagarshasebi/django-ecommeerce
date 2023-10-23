from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import UpdateProfile, RegisterCustomer, LoginForm, AddressForm, DefaultAddressButton,PasswordresetForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordContextMixin
from .models import Address


@login_required()
def customerprofile(request):
    if request.method == 'POST':
        updateform = UpdateProfile(request.POST, instance=request.user)
        if updateform.is_valid():
            updateform.save()
            messages.success(request, f'اکانت شما با موفقیت ویرایش شد.')
            return redirect('profile')
    else:
        updateform = UpdateProfile(instance=request.user)

        context = {'updateform': updateform}
        return render(request, 'users/customer_profile.html', context)

def registercustomer(request):
    if request.method == 'POST':
        register_form = RegisterCustomer(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, f'اکانت شما با  موفقیت ثبت شد')
            return redirect('login')
    else:
        register_form = RegisterCustomer(
        )
    return render(request, 'users/register.html', {'register_form': register_form})


class CustomerLogin(LoginView):
    form_class = LoginForm


class CustomerPasswordReset(PasswordResetView):
    form_class = PasswordresetForm


@login_required
def make_user_address(request):
    if request.method == 'POST':
        Addressform = AddressForm(request.POST)
        if Addressform.is_valid():
            address = Addressform.save(commit=False)
            address.customer = request.user
            address.save()
            return redirect('address')

    else:
        initial_data = {'firstname_customer': request.user.first_name,
                        'lastname_customer': request.user.last_name,
                        'state': '',
                        'county': '',
                        'city': '',
                        'street_address': '',
                        'postal_code': ''}
        Addressform = AddressForm(initial=initial_data)
    return render(request, 'users/address.html', {'Addressform': Addressform})

@login_required
def showaddress(request):

    addresses=Address.objects.filter(customer=request.user)
    return render(request, 'users/show_address.html', {'addresses': addresses})


def set_default_address(request):
    if request.method == 'POST':
        form = DefaultAddressButton(request.POST)
        if form.is_valid():
            address_id = request.POST.get('address_id')
            default_address = form.cleaned_data['default_address']
            Address.objects.filter(customer=request.user).update(default_address=False)
            Address.objects.filter(id=address_id).update(default_address=True)
            return redirect('address')
    return redirect('home')


class PasswordResetConfirmView(PasswordContextMixin,FormView):
    form_class = SetPasswordForm
    title ='Enter new password'
    success_url = reverse_lazy('password_reset_complete')