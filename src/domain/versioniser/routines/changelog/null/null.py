from dataclasses import dataclass

from semver import VersionInfo

from domain.versioniser.routines.changelog.abstract import RoutineChangelog


@dataclass
class Null(RoutineChangelog):
    def run(self, version: VersionInfo) -> None:
        """ This routine does nothing. """

    @staticmethod
    def factory_name() -> str:
        return 'null'
