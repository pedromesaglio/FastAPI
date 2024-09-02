from typing import Union
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse


app = FastAPI()


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Cars",
        "overview": "En un mundo poblado por vehiculos, la carrera de los 400 de Dinoco marca el climax de la ultima temporada de la Copa Piston en el Autodromo de Sur.",
        "year": "2006",
        "rating": 7.2,
        "category": "Sports"
    }
    ]


@app.get("/", tags=['Home'])
def home():
    return {"Hello World"}


@app.get("/movies", tags=['Movies'])
def get_movies():
    return movies 

@app.get("/movies/{id}", tags=['Movies'])
def get_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    return[]


@app.get("/movies/", tags=['Movies'])
def get_movie_by_category(category: str, year: int):
    for movie in movies:
        if movie['category'] == category:
            return movie
    return[]

@app.post('/movies', tags=['Movies'])
def create_movie(id: int = Body(),
                 title: str = Body(),
                 overview: str = Body(),
                 year: int = Body(),
                 rating: float = Body(),
                 category: str = Body()):
    movies.append({
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    })
    return movies

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(
    id: int,
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body()
    ):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview']= overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
    return movies
            
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return movies