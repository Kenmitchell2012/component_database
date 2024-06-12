from django.urls import path

from . import views
from . views import ajax_search


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path('add/', views.AddComponent.as_view(), name='add_component'),
    path('ajax/search/', ajax_search, name='ajax_search'),
    path('edit/<int:pk>/', views.UpdateComponent.as_view(), name='edit_component'),
    path('delete_component/<int:pk>/', views.DeleteComponent.as_view(), name='delete_component'),
    path('<int:pk>/', views.ComponentDetail.as_view(), name='component_detail'),

]