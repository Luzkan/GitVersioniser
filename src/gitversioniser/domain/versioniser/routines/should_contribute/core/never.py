from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.routines.should_contribute.abstract import RoutineShouldContribute


@dataclass
class Never(RoutineShouldContribute):
    def run(self, result: VersioningResult) -> bool:
        return False

    @staticmethod
    def factory_name() -> str:
        return 'never'
