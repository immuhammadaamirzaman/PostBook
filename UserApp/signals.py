from django.db.models.signals import post_save #this sig is fired when user is created 
from django.contrib.auth.models import User # this is sender
from django.dispatch import receiver
from .models import Profile

#this signal will create profile for every user created 

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**krawgs):
    if created:
        Profile.objects.create(user=instance)
    

@receiver(post_save,sender=User)
def save_profile(sender,instance,**krawgs):
    instance.profile.save()
    