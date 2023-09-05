from django.shortcuts import render,redirect
from .forms import UpdateProfile,RegisterCustomer,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView

@login_required()
def customerprofile(request):
    if request.method=='POST':
        updateform= UpdateProfile(request.POST,instance=request.user)
        if updateform.is_valid():
            updateform.save()
            messages.success(request, f'اکانت شما با موفقیت ویرایش شد.')
            return redirect('profile')
    else:
        updateform = UpdateProfile(instance=request.user)

        context = {'updateform': updateform}
        return render(request, 'users/customer_profile.html', context)
# Create your views here.
def registercustomer(request):
    if request.method=='POST':
        register_form=RegisterCustomer(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, f'اکانت شما با  موفقیت ثبت شد')
            return redirect('login')
    else:
        register_form = RegisterCustomer(
        )
    return render(request,'users/register.html',{'register_form': register_form})


class CustomerLogin(LoginView):
    form_class = LoginForm


# Create your views here.
