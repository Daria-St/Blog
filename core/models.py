from django.db import models
from user.models import Profile

class PostCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PostCategory,
                                 blank = True,
                                 null = True,
                                 on_delete=models.SET_NULL,
                                 related_name='category_post')

    profile = models.ForeignKey(Profile,
                                related_name='profile_posts',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


    def __str__(self):
        return self.title

class PostComment(models.Model):
    text = models.TextField(max_length=1000)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='post_comments')
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:10]

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return self.name[:10]

class PostFavorites(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_favorites')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_favorites')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Избранный пост'
        verbose_name_plural = 'Избранные посты'

    def __str__(self):
        return f"{self.post} - {self.profile.user}"