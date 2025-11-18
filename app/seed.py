from .database import Base, engine, SessionLocal
from . import models
Base.metadata.create_all(bind=engine)

# Popula o banco de dados com dados iniciais se estiver vazio
def seed():
    db = SessionLocal()

    # Evita duplicar seed
    if db.query(models.Game).count() > 0:
        return

    # JOGOS 
    g1 = models.Game(
        title="Hades",
        description="Roguelike de ação no submundo da mitologia grega.",
        genre="Action",
        release_year=2020,
        price=73.99,
    )

    g2 = models.Game(
        title="Stardew Valley",
        description="Simulador de fazenda com RPG social.",
        genre="Simulation",
        release_year=2016,
        price=24.99,
    )

    g3 = models.Game(
        title="Portal 2",
        description="Puzzle em primeira pessoa com humor excepcional.",
        genre="Puzzle",
        release_year=2011,
        price=19.99,
    )

    g4 = models.Game(
        title="Hollow Knight",
        description="Metroidvania desafiador no reino de Hallownest.",
        genre="Metroidvania",
        release_year=2017,
        price=29.99,
    )

    g5 = models.Game(
        title="Celeste",
        description="Plataforma preciso com narrativa emocional.",
        genre="Platformer",
        release_year=2018,
        price=39.99,
    )

    db.add_all([g1, g2, g3, g4, g5])
    db.commit()

    # Recarregar com IDs
    games = db.query(models.Game).all()

    #  REVIEWS 
    reviews_data = [
        # HADES
        (g1.id, True, 5, "Incrível gameplay e narrativa envolvente."),
        (g1.id, True, 4, "Desafiador e viciante."),
        (g1.id, True, 5, "Melhor roguelike que já joguei."),
        (g1.id, False, 3, "Muito difícil pra mim."),
        (g1.id, True, 5, "Trilha sonora impecável!"),

        # STARDEW VALLEY
        (g2.id, True, 5, "Relaxante e viciante."),
        (g2.id, True, 5, "O melhor jogo para desestressar."),
        (g2.id, True, 4, "Muito bom, mas fiquei perdido no começo."),
        (g2.id, True, 5, "Personagens carismáticos."),
        (g2.id, False, 3, "Não é meu estilo, mas é bem feito."),

        # PORTAL 2
        (g3.id, True, 5, "Puzzles geniais e humor perfeito."),
        (g3.id, True, 5, "Uma das melhores experiências cooperativas."),
        (g3.id, True, 4, "Roteiro fantástico."),
        (g3.id, False, 3, "Fiquei enjoado com câmera."),
        (g3.id, True, 5, "Clássico absoluto!"),

        # HOLLOW KNIGHT
        (g4.id, True, 5, "Atmosfera e trilha sensacionais."),
        (g4.id, True, 5, "Gameplay fluido e desafiador."),
        (g4.id, False, 3, "Muito difícil."),
        (g4.id, True, 4, "Ótima exploração."),
        (g4.id, True, 5, "Jogo lindo e profundo."),

        # CELESTE
        (g5.id, True, 5, "História emocionante e gameplay preciso."),
        (g5.id, True, 4, "Excelente design de fases."),
        (g5.id, True, 5, "Trilha sonora maravilhosa."),
        (g5.id, False, 3, "Difícil demais, mas bom."),
        (g5.id, True, 5, "Uma obra-prima moderna."),
    ]

    review_objs = [
        models.Review(
            game_id=gid,
            recommended=rec,
            rating=rating,
            comment=comment
        )
        for gid, rec, rating, comment in reviews_data
    ]

    db.add_all(review_objs)
    db.commit()
    db.close()


if __name__ == "__main__":
    seed()
