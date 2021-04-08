from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)



        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'profile.html', context)


def login(request):
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
