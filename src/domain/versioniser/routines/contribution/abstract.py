from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.versioniser.helpers.routine_result import VersionisingResult
from domain.versioniser.routines.abstract import Routine


@dataclass
class RoutineContribution(Routine, ABC):

    @abstractmethod
    def run(self, result: VersionisingResult):
        pass
