from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass
class Never(RoutineTagging):
    def run(self, result: VersioningResult):
        """ This routine does nothing. """

    @staticmethod
    def factory_name() -> str:
        return 'never'
