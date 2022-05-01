from dataclasses import dataclass
from typing import Callable

from semver import VersionInfo

from gitversioniser.helpers.version_bump import VersionBump


@dataclass
class Increment:
    version_bump: VersionBump
    precedence: int
    pattern: str
    bump_version: Callable[[VersionInfo], VersionInfo]

    def __lt__(self, other: 'Increment'):
        """ Allows sorting, mitigating user unwanted behaviour on prerelease versions. """
        return self.precedence < other.precedence

    def __str__(self):
        return self.pattern
