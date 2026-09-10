import httpx

from fastapi import HTTPException

from app.core.config import settings


MATCH_BASE_URL = "https://europe.api.riotgames.com"


QUEUE_MAP = {
    "solo": 420,
    "flex": 440,
    "normal_draft": 400,
    "normal_blind": 430,
}


def get_queue_id(queue: str | None) -> int | None:
    if queue is None or queue == "all":
        return None

    queue_id = QUEUE_MAP.get(queue)

    if queue_id is None:
        raise ValueError(f"Unsupported queue type: {queue}")

    return queue_id


async def get_match_ids(
    puuid: str,
    count: int = 20,
    queue: str | None = None,
) -> list[str]:
    url = (
        f"{MATCH_BASE_URL}"
        f"/lol/match/v5/matches/by-puuid/{puuid}/ids"
    )

    headers = {
        "X-Riot-Token": settings.riot_api_key,
    }

    params = {
        "start": 0,
        "count": count,
    }

    queue_id = get_queue_id(queue)

    if queue_id is not None:
        params["queue"] = queue_id

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers=headers,
            params=params,
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch Riot match IDs",
        )

    return response.json()


async def get_match(
    match_id: str,
) -> dict:
    url = (
        f"{MATCH_BASE_URL}"
        f"/lol/match/v5/matches/{match_id}"
    )

    headers = {
        "X-Riot-Token": settings.riot_api_key,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers=headers,
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Failed to fetch Riot match {match_id}",
        )

    return response.json()