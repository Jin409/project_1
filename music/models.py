from django.db import models


class Song(models.Model):
        songtitle = models.CharField(max_length=30)
        songwriter = models.CharField(max_length=30)
        lyrics = models.TextField()
    
        def __str__(self):
            return self.songtitle
        
