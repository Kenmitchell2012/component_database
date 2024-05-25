from django.urls import path

from . import views



urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path('add/', views.AddComponent.as_view(), name='add_component'),

]