from django.shortcuts import render, redirect
from .forms import CreateUserForm


def home_page(request):
    return render(request, "base/index.html")


def user_register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user-login")

    context = {"registerform": form}

    return render(request, "base/user-register.html", context=context)


def user_login(request):
    return render(request, "base/user-login.html")


def dashboard(request):
    return render(request, "base/dashboard.html")
