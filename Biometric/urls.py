from django.urls import path

from . import views

urlpatterns = [
    path('capture_id/', views.capture_id, name='capture_id'),
]