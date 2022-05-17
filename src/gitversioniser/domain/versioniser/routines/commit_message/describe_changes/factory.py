from gitversioniser.domain.versioniser.routines.commit_message.describe_changes.abstract import DescribeChanges
from gitversioniser.domain.versioniser.routines.commit_message.describe_changes.null import Null
from gitversioniser.domain.versioniser.routines.commit_message.describe_changes.with_emoji import WithEmoji
from gitversioniser.domain.versioniser.routines.commit_message.describe_changes.with_letters import WithLetters
from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.helpers.types import ROUTINE_COMMIT_MESSAGE_DESCRIBE_CHANGES


class DescribeChangesFactory(RoutineFactory):
    @staticmethod
    def create(routine_name: ROUTINE_COMMIT_MESSAGE_DESCRIBE_CHANGES) -> type[DescribeChanges]:
        return {
            RoutineFactory.skip_init(Null).factory_name(): Null,
            RoutineFactory.skip_init(WithEmoji).factory_name(): WithEmoji,
            RoutineFactory.skip_init(WithLetters).factory_name(): WithLetters,
        }[routine_name]
