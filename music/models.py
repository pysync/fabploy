from django.db import models


# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=255)
    album_title = models.CharField(max_length=512)
    genre = models.CharField(max_length=64)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=64)
    song_title = models.CharField(max_length=512)

