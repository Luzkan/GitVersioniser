from dataclasses import dataclass

from rich import print

from gitversioniser.domain.versioniser.routines.version.utils.versions import Versions


@dataclass(frozen=True)
class VersionisingResult:
    versions: Versions
    commit_message: str

    def __post_init__(self):
        print(self)
