import typing
from dataclasses import dataclass

import aiohttp_session
import yaml
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from app.admin.models import Admin

if typing.TYPE_CHECKING:
    from app.web.app import Application


@dataclass
class SessionConfig:
    key: str


@dataclass
class AdminConfig:
    email: str
    password: str


@dataclass
class BotConfig:
    pass


@dataclass
class Config:
    admin: AdminConfig
    session: SessionConfig = None
    bot: BotConfig = None


def setup_config(app: "Application", config_path: str):
    # TODO: добавить BotConfig и SessionConfig по данным из config.yml
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)

    app.config = Config(
        admin=AdminConfig(
            email=raw_config["admin"]["email"],
            password=Admin.hash_password(raw_config["admin"]["password"]),
        ),
        session=SessionConfig(
            key=raw_config["session"]["key"]
        )
    )

