from datetime import datetime

from pydantic import BaseModel


class ChampionResponse(BaseModel):
    id: int


class RunesResponse(BaseModel):
    keystone_id: int
    secondary_style_id: int


class MatchHistoryEntry(BaseModel):
    match_id: str
    queue: str
    game_creation: datetime
    game_duration_seconds: int

    position: str

    champion: ChampionResponse

    win: bool

    kills: int
    deaths: int
    assists: int

    cs: int
    cs_per_minute: float

    items: list[int]

    runes: RunesResponse


class MatchHistoryResponse(BaseModel):
    matches: list[MatchHistoryEntry]