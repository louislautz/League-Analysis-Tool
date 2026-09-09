import httpx

from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.schemas.player import PlayerResolveRequest, PlayerResponse


router = APIRouter(
    prefix="/api/v1/players",
    tags=["players"],
)


@router.post("/resolve", response_model=PlayerResponse)
async def resolve_player(request: PlayerResolveRequest):
    headers = {
        "X-Riot-Token": settings.riot_api_key,
    }

    async with httpx.AsyncClient() as client:
        account_url = (
            "https://europe.api.riotgames.com"
            f"/riot/account/v1/accounts/by-riot-id/"
            f"{request.in_game_name}/{request.tag_line}"
        )

        account_response = await client.get(
            account_url,
            headers=headers,
        )

        if account_response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="Riot account not found",
            )

        if account_response.status_code != 200:
            raise HTTPException(
                status_code=account_response.status_code,
                detail="Riot Account API request failed",
            )

        account_data = account_response.json()

        puuid = account_data["puuid"]

        summoner_url = (
            "https://euw1.api.riotgames.com"
            f"/lol/summoner/v4/summoners/by-puuid/{puuid}"
        )

        summoner_response = await client.get(
            summoner_url,
            headers=headers,
        )

        if summoner_response.status_code != 200:
            raise HTTPException(
                status_code=summoner_response.status_code,
                detail="Riot Summoner API request failed",
            )

        summoner_data = summoner_response.json()

    return PlayerResponse(
        puuid=puuid,
        in_game_name=account_data["gameName"],
        tag_line=account_data["tagLine"],
        profile_icon_id=summoner_data["profileIconId"],
        summoner_level=summoner_data["summonerLevel"],
    )