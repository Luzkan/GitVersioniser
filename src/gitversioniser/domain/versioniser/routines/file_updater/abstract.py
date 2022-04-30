from abc import ABC, abstractmethod

from gitversioniser.domain.versioniser.helpers.versions import Versions
from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.domain.versioniser.routines.file_updater.utils.updated_files import UpdatedFiles


class RoutineFileUpdater(Routine, ABC):

    @abstractmethod
    def run(self, versions: Versions) -> UpdatedFiles:
        pass
