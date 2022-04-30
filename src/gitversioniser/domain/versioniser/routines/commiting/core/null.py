from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.routines.commiting.abstract import RoutineCommiting


@dataclass
class Null(RoutineCommiting):
    def run(self, result: VersioningResult):
        """ This routine does nothing. """

    @staticmethod
    def factory_name() -> str:
        return 'null'
