from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.versioniser.routines.abstract import Routine
from domain.versioniser.routines.version.utils.versions import Versions


@dataclass
class RoutineFileUpdater(Routine, ABC):
    @abstractmethod
    def run(self, versions: Versions) -> None:
        pass
