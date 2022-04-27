from abc import ABC, abstractmethod
from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.domain.versioniser.routines.version.utils.versions import Versions


@dataclass
class RoutineFileUpdater(Routine, ABC):
    @abstractmethod
    def run(self, versions: Versions) -> None:
        pass
