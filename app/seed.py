from .database import Base, engine, SessionLocal
from . import models
Base.metadata.create_all(bind=engine)

def seed():
    db=SessionLocal()
    if db.query(models.Game).count()>0: return
    g1=models.Game(title='Hades',description='Roguelike',genre='Action',release_year=2020,price=73.99)
    g2=models.Game(title='Stardew Valley',description='Fazenda',genre='Sim',release_year=2016,price=24.99)
    db.add_all([g1,g2]); db.commit()
    db.add_all([
        models.Review(game_id=g1.id,recommended=True,rating=5,comment='Incrível'),
        models.Review(game_id=g1.id,recommended=True,rating=4,comment='Difícil mas ótimo'),
        models.Review(game_id=g2.id,recommended=True,rating=5,comment='Relaxante'),
    ]);
    db.commit(); db.close()
if __name__=='__main__': seed()
