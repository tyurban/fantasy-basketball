# SPDX-FileCopyrightText: 2023-present Tyler Urban <tyurban@gmail.com>
#
# SPDX-License-Identifier: MIT
from functools import lru_cache

from pydantic import BaseModel, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class FantasyNerdsEndpointPaths(BaseModel):
    depth_charts: str = 'depth'
    draft_projections: str = 'draft-projections'
    draft_rankings: str = 'draft-rankings'
    injury_reports: str = 'injuries'
    lineups: str = 'lineups'
    nba_teams: str = 'teams'
    news: str = 'news'
    player_rater: str = 'player-rater'
    players: str = 'players'
    schedule: str = 'schedule'


class FantasyNerds(BaseModel):
    base_url: str = 'https://api.fantasynerds.com/v1/nba/'
    api_key: SecretStr = SecretStr('TEST')
    endpoint_paths: FantasyNerdsEndpointPaths = FantasyNerdsEndpointPaths()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter='__', env_file=('.env', '.env.local'))

    fantasy_nerds: FantasyNerds = FantasyNerds()


@lru_cache
def get_settings():
    try:
        return Settings()  # pyright: ignore
    except ValidationError as e:
        raise SystemExit(1) from e


settings = get_settings()
