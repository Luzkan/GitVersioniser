from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.domain.versioniser.routines.version.abstract import RoutineVersion
from gitversioniser.domain.versioniser.routines.version.core import CommitsTillLastGitVersioniserCommit, LastCommit
from gitversioniser.helpers.types import ROUTINE_VERSION_TYPE


class RoutineVersionFactory(RoutineFactory):
    @staticmethod
    def create(routine_version_name: ROUTINE_VERSION_TYPE) -> type[RoutineVersion]:
        return {
            RoutineFactory.skip_init(LastCommit).factory_name(): LastCommit,
            RoutineFactory.skip_init(CommitsTillLastGitVersioniserCommit).factory_name(): CommitsTillLastGitVersioniserCommit,
        }[routine_version_name]
