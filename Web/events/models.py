from django.db import models
from datetime import datetime
#from django.contrib.auth.models import User

class Interest(models.Model):
    game = models.CharField('Interest Game',max_length=20)
    code = models.CharField('Interest Code',max_length=20)
    Hobby = models.CharField('Interest Hobby',max_length=20)
    
    def __str__(self):  #superuser要用的
        return self.game
    
class information(models.Model):
    name = models.CharField('Name',max_length=20)      
    interest = models.ForeignKey(Interest, blank=True, null=True, on_delete=models.CASCADE)
    introduction = models.CharField('Introduction',max_length=50)
    recent_events = models.CharField('Recent_events',max_length=50)
    refresh_date = models.DateTimeField(default=datetime.now, blank=True)
    autobiography = models.TextField('Autobiography',max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.name
        
class paper(models.Model):
    papername = models.CharField('Papername',max_length=100)
    papercontent = models.TextField('Papercontent',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.papername
        
class all_aboutus(models.Model):
    experience = models.CharField('Experience',max_length=100)
    content = models.TextField('Experience',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.experience