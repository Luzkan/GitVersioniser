from dataclasses import dataclass

from gitversioniser.config.increment import Increment
from gitversioniser.helpers.version_bump import VersionBump


@dataclass
class Increments:
    major: Increment = Increment("#major", VersionBump.MAJOR)
    minor: Increment = Increment("#minor", VersionBump.MINOR)
    patch: Increment = Increment("#patch", VersionBump.PATCH)

    def parse_version_bump(self, commit_message: str) -> VersionBump:
        increment: Increment
        for increment in self.__dict__.values():
            if str(increment.pattern) in commit_message:
                return increment.version_bump
        raise ValueError(f"Unknown increment in message: {commit_message}")

    def has_version_bump(self, commit_message: str) -> bool:
        return any([increment.pattern in commit_message for increment in self.__dict__.values()])
