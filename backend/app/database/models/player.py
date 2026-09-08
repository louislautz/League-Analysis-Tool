from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Player(Base):
    __tablename__ = "players"

    puuid: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    in_game_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    tag_line: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    profile_icon_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    summoner_level: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )