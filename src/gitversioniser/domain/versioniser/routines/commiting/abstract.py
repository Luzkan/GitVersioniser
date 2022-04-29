from abc import ABC, abstractmethod

from gitversioniser.domain.versioniser.helpers.routine_result import VersionisingResult
from gitversioniser.domain.versioniser.routines.abstract import Routine


class RoutineCommiting(Routine, ABC):

    @abstractmethod
    def run(self, result: VersionisingResult):
        pass
