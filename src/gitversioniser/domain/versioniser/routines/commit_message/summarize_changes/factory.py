from gitversioniser.domain.versioniser.routines.commit_message.summarize_changes.abstract import SummarizeChanges
from gitversioniser.domain.versioniser.routines.commit_message.summarize_changes.null import Null
from gitversioniser.domain.versioniser.routines.commit_message.summarize_changes.with_emoji_counted import WithEmojiCounted
from gitversioniser.domain.versioniser.routines.commit_message.summarize_changes.with_emoji_symbolic import WithEmojiSymbolic
from gitversioniser.domain.versioniser.routines.commit_message.summarize_changes.with_letters import WithLetters
from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.helpers.types import ROUTINE_COMMIT_MESSAGE_SUMMARIZE_CHANGES


class SummarizeChangesFactory(RoutineFactory):
    @staticmethod
    def create(routine_name: ROUTINE_COMMIT_MESSAGE_SUMMARIZE_CHANGES) -> type[SummarizeChanges]:
        return {
            RoutineFactory.skip_init(Null).factory_name(): Null,
            RoutineFactory.skip_init(WithEmojiCounted).factory_name(): WithEmojiCounted,
            RoutineFactory.skip_init(WithEmojiSymbolic).factory_name(): WithEmojiSymbolic,
            RoutineFactory.skip_init(WithLetters).factory_name(): WithLetters,
        }[routine_name]
