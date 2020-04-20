from django.db import models
from datetime import datetime

class Tv_ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        tv_Show = Tv_Show.objects.filter(title=postData['title'])
        if len(postData['title']) < 3:
            errors["title"] = "title should be at least 3 characters"
        elif len(tv_Show) > 0:
            errors['title'] = " New title is already exists. If that's you, please try"
        
        
        if len(postData['network']) < 3:
            errors["network"] = " network should be at least 3 characters"
        if len(postData['release_date']) < 10:
            errors["release_date"] = " release_date should be filled correctly dd/mm/yyyy"
        if len(postData['descriptions']) < 10:
            errors["descriptions"] = " descriptions should be at list 10 characters"
        return errors
            
        

# Create your models here.
class Tv_Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.TextField()
    descriptions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Tv_ShowManager() 
