from fastapi import FastAPI, Depends, HTTPException
from typing import Optional, List
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from . import crud, schemas

Base.metadata.create_all(bind=engine)
app=FastAPI(title='Steam-like Games API')

@app.get('/')
def root(): return {'msg':'API online'}

@app.get('/games', response_model=List[schemas.GameWithStats])
def games(title:Optional[str]=None, min_price:Optional[float]=None, max_price:Optional[float]=None, min_rating:Optional[float]=None, db:Session=Depends(get_db)):
    res=crud.get_games_with_filters(db,title,min_price,max_price,min_rating)
    out=[]
    for g,avg,t,re in res:
        out.append(schemas.GameWithStats(id=g.id,title=g.title,description=g.description,genre=g.genre,release_year=g.release_year,price=g.price,avg_rating=avg,total_reviews=t or 0,recommended_percentage=re))
    return out

@app.get('/games/{gid}', response_model=schemas.Game)
def game_detail(gid:int, db:Session=Depends(get_db)):
    g=crud.get_game(db,gid)
    if not g: raise HTTPException(404)
    return g

@app.get('/games/{gid}/reviews', response_model=List[schemas.Review])
def revs(gid:int, db:Session=Depends(get_db)):
    if not crud.get_game(db,gid): raise HTTPException(404)
    return crud.get_reviews_for_game(db,gid)
