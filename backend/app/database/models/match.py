from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Match(Base):
    __tablename__ = "matches"

    match_id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    queue_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    game_creation: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    game_duration: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    game_version: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )