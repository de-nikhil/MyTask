from django.shortcuts import render
from django.http import HttpResponse
import tmdbsimple as tmdb
from .models import Movies,Watchlists,Genre


# Create your views here.

def populate(request):
    tmdb.API_KEY = 'e49f9db0cdfb9c51fd3128b065957931' #TMDB api key here
    obj = tmdb.Discover()
    resp = obj.movie(page=1,primary_release_year=2005)  # primary_release_year=2020, with_genres=18, with_original_language='hi'
    pages = resp['total_pages']
    page_no = resp['page']
    total_results = resp['total_results']
    if not Watchlists.objects.filter(codename='Watched'):
        Watchlists.objects.create(codename='Watched')

    for p in range(2, 21): #for p in range(2, pages+1): use this tu pull all relevent data
        resp = obj.movie(page=p, primary_release_year=2005, with_original_language='en')
        li = resp['results']
        for x in li:
            id = x['id']
            if Movies.objects.filter(id_movie=id):
                continue
            original_title = x['original_title']
            if Movies.objects.filter(original_title=original_title):
                continue
            popularity = x['popularity']
            vote_count = x['vote_count']
            video = x['video']
            poster_path = 'https://image.tmdb.org/t/p/w500'+str(x['poster_path'])
            adult = x['adult']
            backdrop_path = '#'
            backdrop_path = x['backdrop_path']
            original_language = x['original_language']
            genre_ids = str(x['genre_ids'])
            title = x['title']
            vote_average = x['vote_average']
            overview = x['overview']
            release_date = x['release_date']
            Movies.objects.create(popularity=popularity,vote_count=vote_count,video=video,poster_path=poster_path,id_movie=id,adult=adult,backdrop_path=backdrop_path,original_language=original_language,original_title=original_title,genre_ids=genre_ids,title=title,vote_average=vote_average,overview=overview,release_date=release_date)
            mobj = Movies.objects.get(id_movie=id)
            for l in x['genre_ids']:
                if not Genre.objects.filter(genre_id=l):
                    Genre.objects.create(genre_id=l)
                gobj = Genre.objects.get(genre_id=l)
                mobj.genre.add(gobj)
    return render(request, 'home.html')


def load_home(request):
    return render(request, 'home.html')

