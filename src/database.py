from sqlalchemy import create_engine
from core.database_config import db_config

engine = create_engine(
    url = db_config.DB_URL_asyncpg,
    echo = True,
)

with engine.connect() as conn:
    res = conn.execute("SELECT VERSION()")
    print(f"{res}")