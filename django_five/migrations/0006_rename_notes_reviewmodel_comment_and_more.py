# Generated by Django 5.0.4 on 2024-05-08 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_five', '0005_contactinfo_reviewmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='notes',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='reviewmodel',
            name='price',
        ),
    ]
