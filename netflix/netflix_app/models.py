from django.db import models
from django.contrib.auth.models import User,AbstractUser,AbstractBaseUser

# Create your models here.


class NetflixProfile(models.Model):
    name = models.CharField(("Profil Adi"), max_length=50)
    avatar = models.ImageField(("Profil Fotoğrafi"), upload_to="Users/Avatars/")
    #hesabın beğendiği,seçtği filmler

    def __str__(self):
        return self.name

class NetflixUser(AbstractUser):
    email = models.EmailField(("E-mail Adresi"), max_length=254,unique=True)
    profile = models.ManyToManyField(NetflixProfile, verbose_name=("Diğer Profiller"))
    