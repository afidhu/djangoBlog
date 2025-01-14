from django.shortcuts import render, redirect

from.forms import registerForm, profileForm, userupdateForm
from django.contrib import messages
from django.contrib import auth
from.models import Profile
from.models import Users
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    forms=registerForm()
    
    if request.method=="POST":
        forms=registerForm(request.POST)
        if forms.is_valid():
            form=forms.save(commit=False)
            form.poster=True
            form.save()
            messages.info(request, 'successfull create account')
            return redirect('login')
        else:
            messages.warning(request, 'Error in creating account!! try again')
            return redirect('register')
    context={
        'form':forms,
    }
    return render(request, 'user/register.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'youre are logout!!!!')
    return redirect('login')




# Create your views here.
@login_required(login_url='login')
def profile(request):
    p_forms=profileForm(instance=request.user)
    #u_forms=userupdateForm(instance=request.user)
    profilee=Profile.objects.filter(author=request.user)
    if request.method=="POST":
        p_forms=profileForm(  request.FILES, instance=request.user)
        #u_forms=userupdateForm(request.POST or None, instance=request.user)
        if p_forms.is_valid():
            form =p_forms.save(commit=False)
            form.author=request.user    
            form.save()    
            messages.info(request, 'successfull edit profile')
            return redirect('dashboard')
        else:
            messages.warning(request, 'error in editing Your profile')
            return redirect('profile')
    context={
        'p_form':p_forms,
        #'u_form':u_forms,
        'profile':profilee,
    }
    return render(request, 'user/profile.html', context)



@login_required(login_url='login')
def deactive(request, pk):
    user=Users.objects.get(id=pk)
    user.is_status = False
    user.save()
    messages.warning(request, 'successfull user Deactiveted by controller')
    return redirect('dashboard')


@login_required(login_url='login')
def active(request, pk):
    user=Users.objects.get(id=pk)
    user.is_status = True
    user.save()
    messages.success(request, 'successfull user actived by controller')
    return redirect('dashboard')


@login_required(login_url='login')
def approved(request, pk):
    user=Users.objects.get(id=pk)
    user.approve = False
    user.save()
    messages.info(request, 'successfull user approved by controller')
    return redirect('dashboard')



def not_approved(request, pk):
    user=Users.objects.get(id=pk)
    user.approve = True
    user.save()
    messages.warning(request, 'successfull user improved by controller')
    return redirect('dashboard')


@login_required(login_url='login')
def user_delete(request, pk):
    user=Users.objects.get(id=pk)
    user.delete()
    messages.warning(request, 'User successfull deleted....')
    return redirect('dashboard')