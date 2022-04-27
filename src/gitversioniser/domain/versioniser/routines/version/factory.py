from gitversioniser.domain.versioniser.routines.version.abstract import RoutineVersion
from gitversioniser.domain.versioniser.routines.version.last_commit import LastCommit
from gitversioniser.domain.versioniser.routines.version.last_gitversioniser_commit import LastGitVersioniserCommit
from gitversioniser.helpers.types import ROUTINE_VERSION_TYPE


class RoutineVersionFactory:
    @staticmethod
    def create(routine_version_name: ROUTINE_VERSION_TYPE) -> type[RoutineVersion]:
        return {
            LastCommit.factory_name(): LastCommit,
            LastGitVersioniserCommit.factory_name(): LastGitVersioniserCommit,
        }[routine_version_name]
