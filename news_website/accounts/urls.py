from django.urls import path, include
from .views import UserRegistrationView, UserVerifyView, LoginView, logoutView

app_name = "accounts"

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("verify/", UserVerifyView.as_view(), name="verify"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logoutView.as_view(), name="logout"),
]
