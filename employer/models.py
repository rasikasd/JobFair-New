from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Jobs(models.Model):
    companyname = models.CharField(max_length=100)
    dateposted = models.DateTimeField(default=timezone.now)
    jobprofile = models.CharField(max_length=80)
    jobplace = models.CharField(max_length=50)
    experience = models.CharField(max_length=30)
    jobdescription = models.TextField(max_length=400)
    contact = models.IntegerField(null=True)
    email = models.EmailField(max_length=30,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    applyHere = models.CharField(max_length=700,null=True)
        
    def __str__(self):
        return self.companyname

    def get_absolute_url(self):
        return reverse('jobs-detail', kwargs={'pk': self.pk})

