from django.db import models

# Create your models here.


class Watchlists(models.Model):
    codename = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
       return self.codename


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.genre_id)


class Movies(models.Model):
    id_movie = models.CharField(max_length=100, primary_key=True)
    popularity = models.DecimalField(max_digits=10, decimal_places=2)
    vote_count = models.IntegerField()
    video = models.CharField(max_length=500)
    poster_path = models.CharField(max_length=100)
    adult = models.CharField(max_length=10)
    backdrop_path = models.CharField(max_length=500, null=True)
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(unique=True, max_length=100)
    genre_ids = models.CharField(max_length=50)
    title = models.CharField(max_length=500)
    vote_average = models.DecimalField(max_digits=10, decimal_places=2)
    overview = models.TextField(max_length=2000)
    release_date = models.DateField()
    code_list = models.ManyToManyField(Watchlists, null=True, blank=True, related_name='+')
    genre = models.ManyToManyField(Genre, null=True, blank=True, related_name='+')

    def __str__(self):
       return self.original_title


