from django.db import models

# Create your models here.
class news(models.Model):
    kun = models.CharField(max_length=255)
    sana = models.DateField()
    nomi = models.CharField(max_length=255)
    malumot = models.TextField()
    rasmi = models.ImageField(upload_to='news')
    telegram = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.nomi



class logo(models.Model):
    nomi = models.CharField(max_length=255)
    rasmi = models.ImageField(upload_to='logo')
    
    def __str__(self):
        return self.nomi