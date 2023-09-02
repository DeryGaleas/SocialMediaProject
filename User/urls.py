from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name="user/logout.html"), name="logout"),
    path("user_update", views.update_user, name="user_update")
]
