from dataclasses import dataclass
from typing import Callable

from gitversioniser.domain.repository.semver_tag import SemverTag


@dataclass(frozen=True)
class Increment:
    precedence: int
    pattern: str
    bump_version: Callable[[SemverTag], SemverTag]

    def __lt__(self, other: 'Increment'):
        """ Allows sorting, mitigating user unwanted behaviour on prerelease versions. """
        return self.precedence < other.precedence

    def __str__(self):
        return self.pattern
