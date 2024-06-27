from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, PredictionForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Prediction
from . import data
import pandas as pd
import joblib

hybrid_model = joblib.load(
    "D:\\PROJECTS\\House Price Prediction System\\house_price_prediction\\model\\hybrid_model.pkl"
)


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
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    context = {"loginform": form}
    return render(request, "base/user-login.html", context=context)


@login_required(login_url="user-login")
def dashboard(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if (
            request.POST.get("city") != ""
            and request.POST.get("location") != ""
            and request.POST.get("area") != ""
            and request.POST.get("bedrooms") != ""
        ):
            # Make prediction
            data = {
                "City": [request.POST.get("city")],
                "Location": [request.POST.get("location")],
                "Area": [float(request.POST.get("area"))],
                "No. of Bedrooms": [int(request.POST.get("bedrooms"))],
            }
            df = pd.DataFrame(data)
            predicted_price = hybrid_model.predict(df)[0]
            predicted_price = round((predicted_price**2) ** 0.5, 0)
            user = request.user
            prediction_instance = Prediction(
                user=user,
                city=data["City"][0],
                location=data["Location"][0],
                area=data["Area"][0],
                bedrooms=data["No. of Bedrooms"][0],
                predicted_price=predicted_price,
            )
            prediction_instance.save()
            return render(
                request,
                "base/results.html",
                {"prediction": predicted_price, "pred_form": form},
            )
        else:
            messages.error(request, "Fill the form completely.")
    else:
        form = PredictionForm()
    return render(request, "base/dashboard.html", {"pred_form": form})


@login_required(login_url="user-login")
def user_logout(request):
    auth.logout(request)
    return redirect("")


@login_required(login_url="user-login")
def get_locations(request, city):
    city_to_locations = data.locations
    locations = city_to_locations.get(city, [])
    return JsonResponse({"locations": locations})


@login_required(login_url="user-login")
def get_history(request):
    user = request.user
    prediction_history = Prediction.objects.filter(user=user).order_by("-date")
    context = {"history": prediction_history}

    return render(request, "base/history.html", context)
