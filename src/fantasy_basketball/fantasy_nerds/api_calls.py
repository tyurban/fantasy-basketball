# SPDX-FileCopyrightText: 2023-present Tyler Urban <tyurban@gmail.com>
#
# SPDX-License-Identifier: MIT
from datetime import date
from typing import Any, Final
from httpx import AsyncClient, Response

from fantasy_basketball.settings import settings

BASE_PARAMS: Final[dict[str, str]] = {'apikey': settings.fantasy_nerds.api_key.get_secret_value()}


async def get_depth_charts(client: AsyncClient) -> dict[str, Any]:
    response: Response = await client.get(
        url=settings.fantasy_nerds.base_url + settings.fantasy_nerds.endpoint_paths.depth_charts, params=BASE_PARAMS,
    )
    response.raise_for_status()
    return response.json()


async def get_draft_projections(client: AsyncClient) -> dict[str, Any]:
    response: Response = await client.get(
        url=settings.fantasy_nerds.base_url + settings.fantasy_nerds.endpoint_paths.draft_projections,
        params=BASE_PARAMS,
    )
    response.raise_for_status()
    return response.json()


async def get_draft_rankings(client: AsyncClient) -> dict[str, Any]:
    response: Response = await client.get(
        url=settings.fantasy_nerds.base_url + settings.fantasy_nerds.endpoint_paths.draft_rankings, params=BASE_PARAMS,
    )
    response.raise_for_status()
    return response.json()


async def get_injury_reports(client: AsyncClient) -> dict[str, Any]:
    response: Response = await client.get(
        url=settings.fantasy_nerds.base_url + settings.fantasy_nerds.endpoint_paths.injury_reports, params=BASE_PARAMS,
    )
    response.raise_for_status()
    return response.json()


async def get_lineups(client: AsyncClient, date: date | None = None) -> dict[str, Any]:
    response: Response = await client.get(
        url=settings.fantasy_nerds.base_url + settings.fantasy_nerds.endpoint_paths.lineups,
        params={**BASE_PARAMS, 'date': date.strftime('%Y-%m-%d') if date else None},
    )
    response.raise_for_status()
    return response.json()


async def get_nba_teams(client: AsyncClient) -> list[dict[str, str]]:
    response: Response = await client.get(
        url=settings.fantasy_nerds.base_url + settings.fantasy_nerds.endpoint_paths.nba_teams, params=BASE_PARAMS,
    )
    response.raise_for_status()
    return response.json()


async def get_news(client: AsyncClient) -> list[dict[str, Any]]:
    response: Response = await client.get(
        url=settings.fantasy_nerds.base_url + settings.fantasy_nerds.endpoint_paths.news, params=BASE_PARAMS,
    )
    response.raise_for_status()
    return response.json()


async def get_player_rater(client: AsyncClient) -> dict[str, Any]:
    response: Response = await client.get(
        url=settings.fantasy_nerds.base_url + settings.fantasy_nerds.endpoint_paths.player_rater, params=BASE_PARAMS,
    )
    response.raise_for_status()
    return response.json()


async def get_players(client: AsyncClient) -> list[dict[str, str]]:
    response: Response = await client.get(
        url=settings.fantasy_nerds.base_url + settings.fantasy_nerds.endpoint_paths.players, params=BASE_PARAMS,
    )
    response.raise_for_status()
    return response.json()


async def get_schedule(client: AsyncClient) -> dict[str, Any]:
    response: Response = await client.get(
        url=settings.fantasy_nerds.base_url + settings.fantasy_nerds.endpoint_paths.schedule, params=BASE_PARAMS,
    )
    response.raise_for_status()
    return response.json()
