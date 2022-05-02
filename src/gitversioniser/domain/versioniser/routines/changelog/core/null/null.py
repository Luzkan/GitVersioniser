from dataclasses import dataclass

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.changelog.abstract import RoutineChangelog


@dataclass
class Null(RoutineChangelog):
    def run(self, new_version: SemverTag) -> None:
        """ This routine does nothing. """

    @staticmethod
    def factory_name() -> str:
        return 'null'
