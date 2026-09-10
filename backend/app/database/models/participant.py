from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Participant(Base):
    __tablename__ = "participants"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    match_id: Mapped[str] = mapped_column(
        ForeignKey("matches.match_id"),
        nullable=False,
    )

    puuid: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    champion_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    team_position: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    win: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    kills: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    deaths: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    assists: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    cs: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    item_0: Mapped[int] = mapped_column(Integer, nullable=False)
    item_1: Mapped[int] = mapped_column(Integer, nullable=False)
    item_2: Mapped[int] = mapped_column(Integer, nullable=False)
    item_3: Mapped[int] = mapped_column(Integer, nullable=False)
    item_4: Mapped[int] = mapped_column(Integer, nullable=False)
    item_5: Mapped[int] = mapped_column(Integer, nullable=False)
    item_6: Mapped[int] = mapped_column(Integer, nullable=False)

    keystone_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    secondary_style_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )