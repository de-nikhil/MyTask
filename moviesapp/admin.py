from django.contrib import admin
from .models import Movies, Watchlists, Genre
# Register your models here.
admin.site.register(Movies)
admin.site.register(Watchlists)
admin.site.register(Genre)
