# Generated by Django 3.2.9 on 2021-12-12 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_rename_image_post_image1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image1',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='imagen',
        ),
    ]
