from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Format(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    length = models.DurationField()
    album_img = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("album_detail", kwargs={"pk": self.pk})
    
class AlbumFormat(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    format = models.ForeignKey(Format, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['album', 'format'], name='unique_album_format')
        ]

    def __str__(self):
        return f"{self.album.title} - {self.format.name} - ${self.price}"
    
class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title    