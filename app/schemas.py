from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# GAMES 
class GameBase(BaseModel):
    title: str
    description: str
    genre: Optional[str] = None
    release_year: Optional[int] = None
    price: float


class Game(GameBase):
    id: int

    class Config:
        orm_mode = True


class GameWithStats(Game):
    avg_rating: Optional[float] = None
    total_reviews: int
    recommended_percentage: Optional[float] = None


# REVIEWS 
class ReviewBase(BaseModel):
    recommended: bool
    rating: int
    comment: str


class Review(ReviewBase):
    id: int
    game_id: int
    created_at: datetime

    class Config:
        orm_mode = True
