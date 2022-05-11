from gitversioniser.domain.versioniser.routines.changelog.abstract import RoutineChangelog
from gitversioniser.domain.versioniser.routines.changelog.core import CommitChangeTags, LastCommitMessageAsDescription, Null
from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.helpers.types import ROUTINE_CHANGELOG_TYPE


class RoutineChangelogFactory(RoutineFactory):
    @staticmethod
    def create(routine_version_name: ROUTINE_CHANGELOG_TYPE) -> type[RoutineChangelog]:
        return {
            RoutineFactory.skip_init(Null).factory_name(): Null,
            RoutineFactory.skip_init(CommitChangeTags).factory_name(): CommitChangeTags,
            RoutineFactory.skip_init(LastCommitMessageAsDescription).factory_name(): LastCommitMessageAsDescription,
        }[routine_version_name]
