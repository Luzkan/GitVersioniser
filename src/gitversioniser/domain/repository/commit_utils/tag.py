from dataclasses import dataclass

from gitversioniser.config.config import Config


@dataclass
class TagUtils:
    config: Config
    value: str
