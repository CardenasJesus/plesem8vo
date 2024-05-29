from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from core.models import Area

# Create your models here.

## SISTEMA DE PROFILES con informacion adicional del usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=128, default="I love plesem system")
    avatar = models.ImageField(null=True, blank=True)
    # area = models.ForeignKey(Area, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    status= models.BooleanField(default=True)
    slug = models.SlugField(max_length=8)


    def __str__(self):
        return self.user.first_name

    
@receiver(post_save, sender=User)
def auto_profile(sender, instance, **kwargs):
    if kwargs.get("created", False):
        Profile.objects.get_or_create(user=instance)