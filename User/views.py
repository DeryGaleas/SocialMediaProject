from django.shortcuts import render, redirect
from .forms import NewUserForm, LoginForm, UpdateUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/post/home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="user/register.html", context={"register_form": form})


def update_user(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UpdateUserForm(instance=request.user)

    return render(request=request, template_name='user/update_user.html', context={"form": form})



