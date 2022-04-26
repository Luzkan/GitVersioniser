from dataclasses import dataclass

from rich import print

from config.credentials import Credentials
from config.patterns import Patterns
from config.routines import Routines


@dataclass
class Config:
    target_repository_path: str
    versioned_files: list[str]
    routines: Routines
    credentials: Credentials = Credentials()
    patterns: Patterns = Patterns()

    def __post_init__(self):
        print(self)
