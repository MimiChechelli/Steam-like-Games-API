from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .database import Base

# Define os modelos de dados para jogos e reviews

class Game(Base):
    __tablename__='games'
    id=Column(Integer, primary_key=True,index=True)
    title=Column(String, index=True, nullable=False)
    description=Column(Text, nullable=False)
    genre=Column(String)
    release_year=Column(Integer)
    price=Column(Float, nullable=False)
    reviews=relationship('Review', back_populates='game')

class Review(Base):
    __tablename__='reviews'
    id=Column(Integer, primary_key=True,index=True)
    game_id=Column(Integer, ForeignKey('games.id'), nullable=False)
    recommended=Column(Boolean, nullable=False)
    rating=Column(Integer, nullable=False)
    comment=Column(Text, nullable=False)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    game=relationship('Game', back_populates='reviews')
