from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse #reverse returns full url as a string 

class Post(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})