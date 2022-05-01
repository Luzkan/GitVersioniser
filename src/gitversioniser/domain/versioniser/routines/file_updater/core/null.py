from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.file_updater.abstract import RoutineFileUpdater
from gitversioniser.domain.versioniser.utils.versions import Versions


@dataclass
class Null(RoutineFileUpdater):
    def run(self, versions: Versions) -> None:
        """ This routine does nothing. """

    @staticmethod
    def factory_name() -> str:
        return 'null'
