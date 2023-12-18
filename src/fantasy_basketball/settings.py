# SPDX-FileCopyrightText: 2023-present Tyler Urban <tyurban@gmail.com>
#
# SPDX-License-Identifier: MIT
from functools import lru_cache

from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter='__', env_file=('.env', '.env.local'))


@lru_cache
def get_settings():
    try:
        return Settings()  # pyright: ignore
    except ValidationError as e:
        raise SystemExit(1) from e


settings = get_settings()
