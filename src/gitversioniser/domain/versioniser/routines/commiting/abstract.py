from abc import ABC, abstractmethod

from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


class RoutineCommiting(Routine, ABC):

    @abstractmethod
    def run(self, result: VersioningResult):
        pass
