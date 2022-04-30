from abc import ABC, abstractmethod

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.routines.abstract import Routine


class RoutineCommiting(Routine, ABC):

    @abstractmethod
    def run(self, result: VersioningResult):
        pass
