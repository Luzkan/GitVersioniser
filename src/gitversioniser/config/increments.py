from dataclasses import dataclass

from gitversioniser.config.increment import Increment
from gitversioniser.helpers.version_bump import VersionBump


@dataclass
class Increments:
    major: Increment = Increment(VersionBump.MAJOR, 1, "#major", lambda version: version.bump_major())
    minor: Increment = Increment(VersionBump.MINOR, 1, "#minor", lambda version: version.bump_minor())
    patch: Increment = Increment(VersionBump.PATCH, 1, "#patch", lambda version: version.bump_patch())
    alpha: Increment = Increment(VersionBump.ALPHA, 2, "#alpha", lambda version: version.bump_prerelease('alpha'))
    beta: Increment = Increment(VersionBump.BETA, 3, "#beta", lambda version: version.bump_prerelease('beta'))
    prerelease: Increment = Increment(VersionBump.PRERELEASE, 4, "#prerelease", lambda version: version.bump_prerelease())
    finalized: Increment = Increment(VersionBump.FINALIZED, 9, "#fin", lambda version: version.finalize_version())

    def parse_increments(self, commit_message: str) -> list[Increment]:
        return [increment for increment in self.__dict__.values() if str(increment.pattern) in commit_message]

    def has_increment(self, commit_message: str) -> bool:
        return any([increment.pattern in commit_message for increment in self.__dict__.values()])
