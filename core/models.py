from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Запись'