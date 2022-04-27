from gitversioniser.domain.versioniser.routines.changelog.abstract import RoutineChangelog
from gitversioniser.domain.versioniser.routines.changelog.commit_pattern.commit_pattern import CommitPattern
from gitversioniser.domain.versioniser.routines.changelog.last_commit_as_summary.last_commit_as_summary import LastCommitAsSummary
from gitversioniser.domain.versioniser.routines.changelog.null.null import Null
from gitversioniser.helpers.types import ROUTINE_CHANGELOG_TYPE


class RoutineChangelogFactory:
    @staticmethod
    def create(routine_version_name: ROUTINE_CHANGELOG_TYPE) -> type[RoutineChangelog]:
        return {
            Null.factory_name(): Null,
            CommitPattern.factory_name(): CommitPattern,
            LastCommitAsSummary.factory_name(): LastCommitAsSummary,
        }[routine_version_name]
