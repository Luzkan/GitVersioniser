from abc import ABC, abstractmethod
from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersionisingResult
from gitversioniser.domain.versioniser.routines.abstract import Routine


@dataclass
class RoutineContribution(Routine, ABC):

    @abstractmethod
    def run(self, result: VersionisingResult):
        pass
