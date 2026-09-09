from pydantic import BaseModel


class PlayerResolveRequest(BaseModel):
    in_game_name: str
    tag_line: str


class PlayerResponse(BaseModel):
    puuid: str
    in_game_name: str
    tag_line: str
    profile_icon_id: int
    summoner_level: int