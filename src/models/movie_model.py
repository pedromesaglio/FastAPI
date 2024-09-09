
import datetime
from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: int
    title: str 
    overview: str
    year: int
    rating: float
    category: str

class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=datetime.date.today().year, ge=1900)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_legth=5, max_legth=20)
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                "title": 'My Movie',
                'overview': 'Esta pelicula trata acerda de ...',
                'year': 2022,
                'rating':5,
                'category': 'Comedia'
            }
        }
    }


class MovieUpdate(BaseModel):
    title: str 
    overview: str
    year: int
    rating: float
    category: str




