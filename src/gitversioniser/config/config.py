from dataclasses import dataclass, field

from gitversioniser.config.credentials import Credentials
from gitversioniser.config.patterns import CommitPatterns
from gitversioniser.config.routines.routines import Routines
from gitversioniser.helpers.logger import CONSOLE


@dataclass(frozen=True)
class Config:
    target_repository_path: str = field(repr=False)
    versioned_files: list[str]
    routines: Routines
    credentials: Credentials = Credentials()
    commit_patterns: CommitPatterns = CommitPatterns()

    def __post_init__(self):
        CONSOLE.rule('Configuration')
        CONSOLE.print(self)
