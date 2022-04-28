from gitversioniser.domain.versioniser.routines.file_updater.abstract import RoutineFileUpdater
from gitversioniser.domain.versioniser.routines.file_updater.core.null import Null
from gitversioniser.domain.versioniser.routines.file_updater.core.versionise_files import VersioniseFiles
from gitversioniser.helpers.types import ROUTINE_FILE_UPDATER_TYPE


class RoutineFileUpdaterFactory:
    @staticmethod
    def create(routine: ROUTINE_FILE_UPDATER_TYPE) -> type[RoutineFileUpdater]:
        return {
            Null.factory_name(): Null,
            VersioniseFiles.factory_name(): VersioniseFiles,
        }[routine]
