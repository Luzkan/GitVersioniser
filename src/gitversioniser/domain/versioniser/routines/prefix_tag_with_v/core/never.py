from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.should_contribute.abstract import RoutineShouldContribute
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass
class Never(RoutineShouldContribute):
    def run(self, result: VersioningResult) -> bool:
        return False

    @staticmethod
    def factory_name() -> str:
        return 'never'
