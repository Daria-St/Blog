from django.contrib import admin
from django.urls import path, include
from .views import *
from .views_rest import *

# создали новый список урл адресов(скопировали из blog/urls)
urlpatterns = [
    path('ajax', ajax, name='api_ajax'),
    path('main/<int:post_id>/favorite', post_favorite, name='api_post_favorite'),
    path('main/<int:post_id>/unfavorite', post_unfavorite, name='api_post_unfavorite'),
    path('feedback', feedback, name='api_feedback'),
    path('rest/feedback_rest', feedback_rest, name='api_feedback_rest'),

    path('<int:post_id>/comments', post_comments, name='api_post_comments'),

    path('rest/<int:post_id>/comments', comments_list_rest, name='comments_list_rest'),
    path('rest/<int:post_id>/comments/add', comments_add_rest, name='comments_add_rest'),

    path('rest/clicks', clicks, name='clicks'),

    path('rest/comments', comments, name='api_rest_comments'),

]