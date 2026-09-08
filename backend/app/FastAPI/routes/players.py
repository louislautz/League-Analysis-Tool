import httpx

from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.schemas.player import PlayerResolveRequest, RiotAccountResponse


router = APIRouter(
    prefix="/api/v1/players",
    tags=["players"],
)


@router.post("/resolve", response_model=RiotAccountResponse)
async def resolve_player(request: PlayerResolveRequest):
    url = (
        "https://europe.api.riotgames.com"
        f"/riot/account/v1/accounts/by-riot-id/"
        f"{request.in_game_name}/{request.tag_line}"
    )

    headers = {
        "X-Riot-Token": settings.riot_api_key,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Riot account not found",
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="Riot API request failed",
        )

    return response.json()