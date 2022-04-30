from gitversioniser.domain.versioniser.routines.changelog.abstract import RoutineChangelog
from gitversioniser.domain.versioniser.routines.changelog.core import CommitPattern, LastCommitMessageAsDescription, Null
from gitversioniser.helpers.types import ROUTINE_CHANGELOG_TYPE


class RoutineChangelogFactory:
    @staticmethod
    def create(routine_version_name: ROUTINE_CHANGELOG_TYPE) -> type[RoutineChangelog]:
        return {
            Null.factory_name(): Null,
            CommitPattern.factory_name(): CommitPattern,
            LastCommitMessageAsDescription.factory_name(): LastCommitMessageAsDescription,
        }[routine_version_name]
