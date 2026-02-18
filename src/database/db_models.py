from src.database.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import MetaData

metadata_obj = MetaData()

class Mwh_users(Base):
    __tablename__ = "mwh_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    tg_id: Mapped[int] = mapped_column(unique=True)
    role: Mapped[None | str] = mapped_column(nullable=True)