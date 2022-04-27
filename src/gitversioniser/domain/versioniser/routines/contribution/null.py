from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersionisingResult
from gitversioniser.domain.versioniser.routines.contribution.abstract import RoutineContribution


@dataclass
class Null(RoutineContribution):
    def run(self, result: VersionisingResult):
        """ This routine does nothing. """

    @staticmethod
    def factory_name() -> str:
        return 'null'
