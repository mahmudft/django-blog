# Generated by Django 2.2 on 2019-04-30 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
