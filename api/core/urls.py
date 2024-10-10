from django.contrib import admin
from django.urls import path, include
from .views import *

# создали новый список урл адресов(скопировали из blog/urls)
urlpatterns = [
    path('ajax', ajax, name='api_ajax'),
    path('main/<int:post_id>/favorite', post_favorite, name='api_post_favorite'),
    path('main/<int:post_id>/unfavorite', post_unfavorite, name='api_post_unfavorite'),

]