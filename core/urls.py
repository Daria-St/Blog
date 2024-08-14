from django.contrib import admin
from django.urls import path, include

from .views import main, posts

urlpatterns = [
    path('', main),
    # path('posts', posts),
]