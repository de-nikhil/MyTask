# VesatGo task

Graphql API using Django and Postgresql.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python libraries.

```bash
pip install django
pip install tmdbsimple
pip install psycopg2
pip install graphene-django
```

## Usage

```graphql
#use graphiql interface to test graphql queries.

#query to get all movies with details
query{
  allMovies{
    originalTitle
  }
}

#query for getting spec=sific movie details by id
query{
  moviebyid(id:9981){
    originalTitle
    codeList{
      codename
    }
  
  }
}

#mutaion to create a custom list
mutation{
  CreateCodename(codename:"Horror"){
    codename
  }
}

#mutaion to add movie to existing list
mutation{
  PushMovie(codename:"Horror",name:"The Ringer"){
    originalTitle
  }
}

#query to get recommended movies by providing existing list
# query{
#   reccomendByCodename(name:"Horror"){
#     originalTitle
#   }
# }
```

## Help
Contact deshm.nikhil@gmail.com