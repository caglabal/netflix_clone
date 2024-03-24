# Generated by Django 5.0.3 on 2024-03-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix_app', '0004_alter_netflixuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetflixProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Profil Adi')),
                ('avatar', models.ImageField(upload_to='Users/Avatars/', verbose_name='Profil Fotoğrafi')),
            ],
        ),
        migrations.RemoveField(
            model_name='netflixuser',
            name='avatar',
        ),
    ]