from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.domain.versioniser.routines.file_updater.abstract import RoutineFileUpdater
from gitversioniser.domain.versioniser.routines.file_updater.core import Null, VersioniseFiles
from gitversioniser.helpers.types import ROUTINE_FILE_UPDATER_TYPE


class RoutineFileUpdaterFactory(RoutineFactory):
    @staticmethod
    def create(routine: ROUTINE_FILE_UPDATER_TYPE) -> type[RoutineFileUpdater]:
        return {
            RoutineFactory.skip_init(Null).factory_name(): Null,
            RoutineFactory.skip_init(VersioniseFiles).factory_name(): VersioniseFiles,
        }[routine]
