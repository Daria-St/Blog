from django.contrib import admin
from django.urls import path, include

from .views import main,  post_add

urlpatterns = [
    path('', main, name='main'),
    path('add', post_add, name='post_add'),
]