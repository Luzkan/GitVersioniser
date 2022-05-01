from dataclasses import dataclass, field

from rich import print

from gitversioniser.config.credentials import Credentials
from gitversioniser.config.patterns import Patterns
from gitversioniser.config.routines import Routines


@dataclass
class Config:
    target_repository_path: str = field(repr=False)
    versioned_files: list[str]
    routines: Routines
    credentials: Credentials = Credentials()
    patterns: Patterns = field(default=Patterns(), repr=False)

    def __post_init__(self):
        print(self)
