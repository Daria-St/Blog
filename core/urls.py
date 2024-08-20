from django.contrib import admin
from django.urls import path, include

from .views import main,  post_add, post_add_submit

urlpatterns = [
    path('', main, name='main'),
    path('main/add', post_add),
    path('main/add_submit', post_add_submit, name='post_add_submit'),
]