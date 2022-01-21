from django.urls import path
from .views import index, edit
urlpatterns = [
    path('', index),
    path('edit/<int:number>/', edit)
]