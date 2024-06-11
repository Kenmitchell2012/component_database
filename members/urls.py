from django.urls import path
from .views import auth_view, sign_in_view, register_view

urlpatterns = [
    path('auth/', auth_view, name='auth'),
    path('signin/', sign_in_view, name='sign_in'),
    path('register/', register_view, name='register'),
]
