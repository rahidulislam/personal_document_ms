from django.urls import path
from django.urls import path
from .views import UserRegistrationView, UserLoginView

app_name = 'account'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
]
