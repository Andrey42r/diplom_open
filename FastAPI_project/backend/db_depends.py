from .db import SessionLocal

async def get_db():
    """

    Зависимость для сеанса работы с базой данных

    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()