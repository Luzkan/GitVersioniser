from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage
from gitversioniser.domain.versioniser.routines.commit_message.core import (
    Null,
    PrefixVersionFull,
    PrefixVersionFullOnlyNumbers,
    PrefixVersionMajorMinorPatch,
    PrefixVersionMajorMinorPatchPrerelease,
    SuffixVersionFull,
    SuffixVersionFullOnlyNumbers,
    SuffixVersionMajorMinorPatch,
    SuffixVersionMajorMinorPatchPrerelease,
)
from gitversioniser.helpers.types import ROUTINE_COMMIT_MESSAGE_TYPE


class RoutineCommitMessageFactory:
    @staticmethod
    def create(routine_commit_name: ROUTINE_COMMIT_MESSAGE_TYPE) -> type[RoutineCommitMessage]:
        return {
            Null.factory_name(): Null,
            PrefixVersionFull.factory_name(): PrefixVersionFull,
            PrefixVersionFullOnlyNumbers.factory_name(): PrefixVersionFullOnlyNumbers,
            PrefixVersionMajorMinorPatch.factory_name(): PrefixVersionMajorMinorPatch,
            PrefixVersionMajorMinorPatchPrerelease.factory_name(): PrefixVersionMajorMinorPatchPrerelease,
            SuffixVersionFull.factory_name(): SuffixVersionFull,
            SuffixVersionFullOnlyNumbers.factory_name(): SuffixVersionFullOnlyNumbers,
            SuffixVersionMajorMinorPatch.factory_name(): SuffixVersionMajorMinorPatch,
            SuffixVersionMajorMinorPatchPrerelease.factory_name(): SuffixVersionMajorMinorPatchPrerelease,
        }[routine_commit_name]
