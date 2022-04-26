from domain.versioniser.routines.file_updater.abstract import RoutineFileUpdater
from domain.versioniser.routines.file_updater.null import Null
from domain.versioniser.routines.file_updater.versionise_files import VersioniseFiles
from helpers.types import ROUTINE_FILE_UPDATER_TYPE


class RoutineFileUpdaterFactory:
    @staticmethod
    def create(routine: ROUTINE_FILE_UPDATER_TYPE) -> type[RoutineFileUpdater]:
        return {
            Null.factory_name(): Null,
            VersioniseFiles.factory_name(): VersioniseFiles,
        }[routine]
