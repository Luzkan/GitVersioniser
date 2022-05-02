from dataclasses import dataclass

from gitversioniser.domain.repository.semver_tag import SemverTag


@dataclass
class Versions:
    old: SemverTag
    new: SemverTag
