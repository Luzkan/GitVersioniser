from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.should_contribute.abstract import RoutineShouldContribute
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass
class Always(RoutineShouldContribute):
    def run(self, result: VersioningResult) -> bool:
        return True

    @staticmethod
    def factory_name() -> str:
        return 'always'
