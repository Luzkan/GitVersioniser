from abc import ABC, abstractmethod

from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


class RoutineTagging(Routine, ABC):
    @abstractmethod
    def run(self, result: VersioningResult) -> None:
        pass
