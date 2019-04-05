from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from .forms import UserRegisterForm


class Register(View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/registration_page.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Konto stworzone dla {}!. Zaloguj się'.format(username))
            return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'users/registration_page.html', {'form': form})

@login_required()
def profile(request):
    if request.method == "GET":
                return render(request, 'users/profile.html')


