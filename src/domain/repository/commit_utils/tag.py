from dataclasses import dataclass

from config.config import Config


@dataclass
class TagUtils:
    config: Config
    value: str
