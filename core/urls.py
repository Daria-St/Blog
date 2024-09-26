from django.contrib import admin
from django.urls import path, include

from .views import main,  post_add, post_detail, feedback_add, feedback_done, post_favorite, post_unfavorite

urlpatterns = [
    path('', main, name='main'),
    path('add', post_add, name='post_add'),
    path('<int:post_id>', post_detail, name='post_detail'),
    path('feedback_add', feedback_add, name='feedback_add'),
    path('feedback_done', feedback_done, name='feedback_done'),

    path('favorite/<int:post_id>', post_favorite, name='post_favorite'),
    path('unfavorite/<int:post_id>', post_unfavorite, name='post_unfavorite')
]