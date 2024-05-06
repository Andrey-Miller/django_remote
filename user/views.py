from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserForm
from .models import User


def fetch_user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})


def fetch_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user/user_detail.html', {'user': user})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            user = User(
                name=name,
                email=email,
                phone_number=phone_number,
                address=address
            )
            user.save()
            return redirect('user_list')
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'user/add_user.html', {'form': form, 'message': message})


def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user.name = form.cleaned_data['name']
            user.email = form.cleaned_data['email']
            user.phone_number = form.cleaned_data['phone_number']
            user.address = form.cleaned_data['address']
            user.save()
            return redirect('user_list')
    else:
        form = UserForm(initial={
            'name': user.name,
            'email': user.email,
            'phone_number': user.phone_number,
            'address': user.address
        })
    return render(request, 'user/edit_user.html', {'form': form, 'user': user})
