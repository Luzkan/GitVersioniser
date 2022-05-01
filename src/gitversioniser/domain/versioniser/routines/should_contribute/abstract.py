from abc import ABC, abstractmethod

from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


class RoutineShouldContribute(Routine, ABC):

    @abstractmethod
    def run(self, result: VersioningResult) -> bool:
        pass
