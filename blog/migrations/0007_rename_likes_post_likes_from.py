# Generated by Django 3.2.8 on 2021-10-26 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_likes_count_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='likes_from',
        ),
    ]
