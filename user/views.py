from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CreationForm
from .models import User


def registration(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # сохранение номера
            User.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            #raw_password = form.cleaned_data.get('password1')
            user = authenticate(phone_number=user.phone_number)
            login(request, user)
            return redirect('/')
    else:
        form = CreationForm()
    return render(request, 'user/signup.html', {'form': form})