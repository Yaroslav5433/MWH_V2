from .database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Mwh_users(Base):
    __tablename__ = "Mwh_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    tg_id: Mapped[int]
    role: Mapped[None | str]