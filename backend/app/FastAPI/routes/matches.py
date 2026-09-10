from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.match import Match
from app.database.models.participant import Participant
from app.database.session import get_db
from app.RiotAPI.match import get_match_ids, get_match
from app.schemas.match import (
    ChampionResponse,
    MatchHistoryEntry,
    MatchHistoryResponse,
    RunesResponse,
)


router = APIRouter(
    prefix="/api/v1/players",
    tags=["matches"],
)


@router.get(
    "/{puuid}/matches",
    response_model=MatchHistoryResponse,
)
async def get_player_matches(
    puuid: str,
    queue: str = Query(default="solo"),
    count: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    match_ids = await get_match_ids(
        puuid=puuid,
        count=count,
        queue=queue,
    )

    history = []

    for match_id in match_ids:
        match = db.get(Match, match_id)

        participant = db.scalar(
            select(Participant).where(
                Participant.match_id == match_id,
                Participant.puuid == puuid,
            )
        )

        # We don't have this match locally yet
        if match is None or participant is None:
            riot_match = await get_match(match_id)

            info = riot_match["info"]

            if match is None:
                match = Match(
                    match_id=match_id,
                    queue_id=info["queueId"],
                    game_creation=datetime.fromtimestamp(
                        info["gameCreation"] / 1000,
                        tz=timezone.utc,
                    ),
                    game_duration=info["gameDuration"],
                    game_version=info["gameVersion"],
                )

                db.add(match)

            # Store every participant in the match
            for riot_participant in info["participants"]:
                existing_participant = db.scalar(
                    select(Participant).where(
                        Participant.match_id == match_id,
                        Participant.puuid == riot_participant["puuid"],
                    )
                )

                if existing_participant is not None:
                    continue

                participant_row = Participant(
                    match_id=match_id,
                    puuid=riot_participant["puuid"],
                    champion_id=riot_participant["championId"],
                    team_position=riot_participant["teamPosition"],
                    win=riot_participant["win"],
                    kills=riot_participant["kills"],
                    deaths=riot_participant["deaths"],
                    assists=riot_participant["assists"],
                    cs=(
                        riot_participant["totalMinionsKilled"]
                        + riot_participant["neutralMinionsKilled"]
                    ),
                    item_0=riot_participant["item0"],
                    item_1=riot_participant["item1"],
                    item_2=riot_participant["item2"],
                    item_3=riot_participant["item3"],
                    item_4=riot_participant["item4"],
                    item_5=riot_participant["item5"],
                    item_6=riot_participant["item6"],
                    keystone_id=riot_participant["perks"]["styles"][0]["selections"][0]["perk"],
                    secondary_style_id=riot_participant["perks"]["styles"][1]["style"],
                )

                db.add(participant_row)

            db.commit()

            # Now retrieve the requested player's participant row
            participant = db.scalar(
                select(Participant).where(
                    Participant.match_id == match_id,
                    Participant.puuid == puuid,
                )
            )

        cs_per_minute = (
            participant.cs / (match.game_duration / 60)
            if match.game_duration > 0
            else 0
        )

        history.append(
            MatchHistoryEntry(
                match_id=match.match_id,
                queue=queue,
                game_creation=match.game_creation,
                game_duration_seconds=match.game_duration,
                position=participant.team_position,
                champion=ChampionResponse(
                    id=participant.champion_id,
                ),
                win=participant.win,
                kills=participant.kills,
                deaths=participant.deaths,
                assists=participant.assists,
                cs=participant.cs,
                cs_per_minute=round(cs_per_minute, 2),
                items=[
                    participant.item_0,
                    participant.item_1,
                    participant.item_2,
                    participant.item_3,
                    participant.item_4,
                    participant.item_5,
                    participant.item_6,
                ],
                runes=RunesResponse(
                    keystone_id=participant.keystone_id,
                    secondary_style_id=participant.secondary_style_id,
                ),
            )
        )

    return MatchHistoryResponse(
        matches=history,
    )