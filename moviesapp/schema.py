import graphene
from graphene_django.types import DjangoObjectType
from .models import Movies, Watchlists, Genre


class MoviesType(DjangoObjectType):
    class Meta:
        model = Movies


class WatchlistsType(DjangoObjectType):
    class Meta:
        model = Watchlists


class GenreType(DjangoObjectType):
    class Meta:
        model = Genre


class Query(object):
    all_movies = graphene.List(MoviesType)
    moviebyid = graphene.Field(MoviesType, id=graphene.Int())
    movie_by_codelist = graphene.List(MoviesType, name=graphene.String())
    reccomend_by_codename = graphene.List(MoviesType,  name=graphene.String())

    def resolve_all_movies(self, info):
        return Movies.objects.all()

    def resolve_moviebyid(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Movies.objects.get(id_movie=id)
        else:
            return None

    def resolve_movie_by_codelist(self, info, **kwargs):
        name = kwargs.get('name')
        if name is not None:
            return Movies.objects.filter(code_list=name)
        else:
            return None

    def resolve_reccomend_by_codename(self,info,**kwargs):
        name = kwargs.get('name')
        if name is  None:
            return None
        obj = Movies.objects.filter(code_list=name)
        idlist = []
        for x in obj:
            data = x.genre.values()
            for data2 in data:
                print(data2['genre_id'])
                if data2['genre_id'] not in idlist:
                    idlist.append(data2['genre_id'])
        print(idlist)
        return Movies.objects.filter(genre__in=idlist).order_by('-popularity')[:10]


class CreateCodename(graphene.Mutation):
    codename = graphene.String()

    class Arguments:
        codename = graphene.String()

    def mutate(self, info, codename):
        obj = Watchlists(codename=codename)
        obj.save()

        return CreateCodename(codename=obj.codename)


class PushMovie(graphene.Mutation):
    codename = graphene.String()
    name = graphene.String()
    original_title = graphene.String()

    class Arguments:
        codename = graphene.String()
        name = graphene.String()

    def mutate(self, info, codename, name):
        obj = Movies.objects.get(original_title=name)
        wobj = Watchlists.objects.get(codename=codename)
        print(wobj.codename)
        obj.code_list.add(wobj)
        obj.save()
        return PushMovie(original_title=obj.original_title)


class Mutation(graphene.ObjectType):
    Create_Codename = CreateCodename.Field()
    Push_Movie = PushMovie.Field()