from gitversioniser.domain.versioniser.routines.version.abstract import RoutineVersion
from gitversioniser.domain.versioniser.routines.version.core.commits_till_last_gitversioniser_commit import CommitsTillLastGitVersioniserCommits
from gitversioniser.domain.versioniser.routines.version.core.last_commit import LastCommit
from gitversioniser.helpers.types import ROUTINE_VERSION_TYPE


class RoutineVersionFactory:
    @staticmethod
    def create(routine_version_name: ROUTINE_VERSION_TYPE) -> type[RoutineVersion]:
        return {
            LastCommit.factory_name(): LastCommit,
            CommitsTillLastGitVersioniserCommits.factory_name(): CommitsTillLastGitVersioniserCommits,
        }[routine_version_name]
