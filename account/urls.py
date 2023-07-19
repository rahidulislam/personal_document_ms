from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserRegistrationView, UserLoginView

app_name = 'account'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('token/', UserLoginView.as_view(), name='user_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
