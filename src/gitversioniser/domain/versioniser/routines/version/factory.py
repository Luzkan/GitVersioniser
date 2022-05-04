from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.domain.versioniser.routines.version.abstract import RoutineVersion
from gitversioniser.domain.versioniser.routines.version.core import VersionTagInCommitsTillLastGitVersioniserCommit, VersionTagInLastCommit
from gitversioniser.helpers.types import ROUTINE_VERSION_TYPE


class RoutineVersionFactory(RoutineFactory):
    @staticmethod
    def create(routine_version_name: ROUTINE_VERSION_TYPE) -> type[RoutineVersion]:
        return {
            RoutineFactory.skip_init(VersionTagInLastCommit).factory_name(): VersionTagInLastCommit,
            RoutineFactory.skip_init(VersionTagInCommitsTillLastGitVersioniserCommit).factory_name(): VersionTagInCommitsTillLastGitVersioniserCommit
        }[routine_version_name]
