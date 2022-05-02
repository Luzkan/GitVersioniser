from abc import ABC, abstractmethod

from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.domain.versioniser.utils.versions import Versions


class RoutinePrefixTagWithV(Routine, ABC):

    @abstractmethod
    def run(self, versions: Versions) -> bool:
        pass
