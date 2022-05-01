from abc import ABC, abstractmethod

from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.domain.versioniser.routines.file_updater.utils.updated_files import UpdatedFiles
from gitversioniser.domain.versioniser.utils.versions import Versions


class RoutineFileUpdater(Routine, ABC):

    @abstractmethod
    def run(self, versions: Versions) -> UpdatedFiles:
        pass
