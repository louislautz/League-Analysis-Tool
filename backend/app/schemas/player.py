from pydantic import BaseModel


class PlayerResolveRequest(BaseModel):
    in_game_name: str
    tag_line: str


class RiotAccountResponse(BaseModel):
    puuid: str
    gameName: str
    tagLine: str