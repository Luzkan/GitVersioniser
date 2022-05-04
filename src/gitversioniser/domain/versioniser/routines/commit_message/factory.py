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
from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.helpers.types import ROUTINE_COMMIT_MESSAGE_TYPE


class RoutineCommitMessageFactory(RoutineFactory):
    @staticmethod
    def create(routine_commit_name: ROUTINE_COMMIT_MESSAGE_TYPE) -> type[RoutineCommitMessage]:
        return {
            RoutineFactory.skip_init(Null).factory_name(): Null,
            RoutineFactory.skip_init(PrefixVersionFull).factory_name(): PrefixVersionFull,
            RoutineFactory.skip_init(PrefixVersionFullOnlyNumbers).factory_name(): PrefixVersionFullOnlyNumbers,
            RoutineFactory.skip_init(PrefixVersionMajorMinorPatch).factory_name(): PrefixVersionMajorMinorPatch,
            RoutineFactory.skip_init(PrefixVersionMajorMinorPatchPrerelease).factory_name(): PrefixVersionMajorMinorPatchPrerelease,
            RoutineFactory.skip_init(SuffixVersionFull).factory_name(): SuffixVersionFull,
            RoutineFactory.skip_init(SuffixVersionFullOnlyNumbers).factory_name(): SuffixVersionFullOnlyNumbers,
            RoutineFactory.skip_init(SuffixVersionMajorMinorPatch).factory_name(): SuffixVersionMajorMinorPatch,
            RoutineFactory.skip_init(SuffixVersionMajorMinorPatchPrerelease).factory_name(): SuffixVersionMajorMinorPatchPrerelease,
        }[routine_commit_name]
