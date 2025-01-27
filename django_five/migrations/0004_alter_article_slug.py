# Generated by Django 5.0.4 on 2024-05-07 19:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_five', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]
