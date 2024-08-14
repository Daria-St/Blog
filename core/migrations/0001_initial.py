# Generated by Django 5.1 on 2024-08-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Запись',
            },
        ),
    ]