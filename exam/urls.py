from django.urls import path
from .views import index, edit
urlpatterns = [
    path('', index, name='main'),
    path('edit/<int:number>/', edit)
]