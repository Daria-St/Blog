from django.contrib import admin

from .models import Post, PostCategory, PostComment
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(PostComment)