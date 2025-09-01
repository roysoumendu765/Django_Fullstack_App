from django.db import models

class Playlist(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title

class videoList(models.Model):
    title= models.TextField()
    artist= models.TextField()
    video_file = models.FileField(blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title