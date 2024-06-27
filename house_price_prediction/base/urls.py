from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name=""),
    path("user-register", views.user_register, name="user-register"),
    path("user-login", views.user_login, name="user-login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("user-logout", views.user_logout, name="user-logout"),
    path('get-locations/<str:city>/', views.get_locations, name='get_locations'),
]
