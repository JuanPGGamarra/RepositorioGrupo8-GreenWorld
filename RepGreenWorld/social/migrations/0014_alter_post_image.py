# Generated by Django 3.2.9 on 2021-12-13 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
