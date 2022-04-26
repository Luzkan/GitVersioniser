from domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage
from domain.versioniser.routines.commit_message.null import Null
from domain.versioniser.routines.commit_message.prefix_tag import PrefixTag
from domain.versioniser.routines.commit_message.suffix_tag import SuffixTag
from helpers.types import ROUTINE_COMMIT_MESSAGE_TYPE


class RoutineCommitFactory:
    @staticmethod
    def create(routine_commit_name: ROUTINE_COMMIT_MESSAGE_TYPE) -> type[RoutineCommitMessage]:
        return {
            Null.factory_name(): Null,
            PrefixTag.factory_name(): PrefixTag,
            SuffixTag.factory_name(): SuffixTag,
        }[routine_commit_name]
