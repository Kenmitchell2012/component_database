from django.urls import path

from . import views
from . views import ajax_search


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path('add/', views.AddComponent.as_view(), name='add_component'),
    path('ajax/search/', ajax_search, name='ajax_search'),

]