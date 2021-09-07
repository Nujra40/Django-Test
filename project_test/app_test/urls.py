from django.urls import path
from . import views

urlpatterns = [
    path('', views.greet, name="index"),
    path('<str:user>', views.greet, name='greet')
]