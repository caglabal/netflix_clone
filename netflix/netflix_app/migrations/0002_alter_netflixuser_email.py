# Generated by Django 5.0.3 on 2024-03-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netflixuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail Adresi'),
        ),
    ]
