# Generated by Django 5.1.6 on 2025-02-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog_images/'),
        ),
    ]
