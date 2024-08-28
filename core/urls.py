from django.contrib import admin
from django.urls import path, include

from .views import main,  post_add, post_detail, comment_add

urlpatterns = [
    path('', main, name='main'),
    path('add', post_add, name='post_add'),
    path('<int:post_id>', post_detail, name='post_detail'),
    path('<int:post_id>/comment/add', comment_add, name='comment_add'),
]