from domain.versioniser.routines.version.abstract import RoutineVersion
from domain.versioniser.routines.version.last_commit import LastCommit
from domain.versioniser.routines.version.last_gitversioniser_commit import LastGitVersioniserCommit
from helpers.types import ROUTINE_VERSION_TYPE


class RoutineVersionFactory:
    @staticmethod
    def create(routine_version_name: ROUTINE_VERSION_TYPE) -> type[RoutineVersion]:
        return {
            LastCommit.factory_name(): LastCommit,
            LastGitVersioniserCommit.factory_name(): LastGitVersioniserCommit,
        }[routine_version_name]
