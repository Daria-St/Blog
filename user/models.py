from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(User,
                             on_delete=models.CASCADE
                             )

    about = models.TextField(verbose_name='Обо мне')

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'
    def __str__(self):
        return self.user.username

