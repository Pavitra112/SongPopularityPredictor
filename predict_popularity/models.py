from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Popularity_Predictions(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE,related_name='popularitypredict') 
    Title = models.CharField(max_length=50)
    Artist = models.CharField(max_length=25)
    Year = models.IntegerField()
    bpm = models.IntegerField()
    Energy = models.IntegerField()
    Danceability = models.IntegerField()
    Loudness = models.IntegerField()
    Liveness = models.IntegerField()
    Valence =  models.IntegerField()
    Duration = models.IntegerField()
    Acousticness = models.IntegerField()
    Speechiness = models.IntegerField()
    result = models.IntegerField(default=0)
    def get_absolute_url(self):
        return reverse('predict:predict', kwargs={'pk': self.profile.pk})
    
    def __str__(self):
        return self.Title
    