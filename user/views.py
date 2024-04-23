from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from .models import User


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            User.objects.create(phone_number=form.cleaned_data.get('phone_number'))
            user = authenticate(phone_number=user.phone_number)
            user.save()
            login(request, user)
            return redirect('user:profile', request.user.phone_number)
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/signup.html', {'form': form})


def profile(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('user:signup')
    invite_code = user.invite_code
    invited_users = User.objects.filter(invite_code=invite_code)
    context = {
        'user': user,
        'invited_users': invited_users
    }
    return render(request, 'user/profile.html', context)

