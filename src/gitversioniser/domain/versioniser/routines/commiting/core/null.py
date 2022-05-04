from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.commiting.abstract import RoutineCommiting
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass
class Null(RoutineCommiting):
    def run(self, result: VersioningResult):
        """ This routine does nothing. """
