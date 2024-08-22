from django.db import models

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

    class Meta:
        verbose_name = 'Запись'

    def __str__(self):
        return self.title