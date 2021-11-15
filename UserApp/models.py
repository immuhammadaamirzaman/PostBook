from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def save(self,*args,**kwargs):#overridding the save method 
        super().save()

        img=Image.open(self.image.path)

        if img.height > 300 or img.width>300:
            img_size=(300,300)
            img.thumbnail(img_size)
            img.save(self.image.path)