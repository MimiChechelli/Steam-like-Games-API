from sqlalchemy.orm import Session
from sqlalchemy import func, Float
from . import models
from typing import Optional

def get_game(db:Session, game_id:int): # Busca um jogo pelo ID
    return (
        db.query(models.Game)
        .filter(models.Game.id==game_id)
        .first())

def get_games_with_filters(db:Session, title=None, min_price=None, max_price=None, min_rating=None):
    stats = (
        db.query(
            models.Review.game_id.label("game_id"),
            func.avg(models.Review.rating).label("avg_rating"), # Média das avaliações
            func.count(models.Review.id).label("total_reviews"), # Total de avaliações
            func.avg(func.cast(models.Review.recommended, Float)).label("rec_ratio"), # Média de recomendações
        )
        .group_by(models.Review.game_id)
        .subquery()
    )

    # Query principal juntando jogos com as estatísticas
    q = (
        db.query(
            models.Game,
            stats.c.avg_rating,
            stats.c.total_reviews,
            (stats.c.rec_ratio * 100).label("rec_pct"),
        )
        .outerjoin(stats, models.Game.id == stats.c.game_id)
    )

    if title: 
        q=q.filter(models.Game.title.ilike(f"%{title}%"))
    if min_price is not None: 
        q=q.filter(models.Game.price>=min_price)
    if max_price is not None: 
        q=q.filter(models.Game.price<=max_price)
    if min_rating is not None: 
        q=q.filter(stats.c.avg_rating>=min_rating)
    return q.all()

def get_reviews_for_game(db: Session, game_id: int): # Busca todas as reviews de um jogo pelo ID do jogo
    return (
        db.query(models.Review)
        .filter(models.Review.game_id == game_id)
        .order_by(models.Review.created_at.desc())
        .all()
    )