
from gitversioniser.domain.versioniser.routines.commit_message.format_version_tag.abstract import FormatVersionTag
from gitversioniser.domain.versioniser.routines.commit_message.format_version_tag.full import Full
from gitversioniser.domain.versioniser.routines.commit_message.format_version_tag.full_but_only_digits import FullButOnlyDigits
from gitversioniser.domain.versioniser.routines.commit_message.format_version_tag.major_minor_patch import MajorMinorPatch
from gitversioniser.domain.versioniser.routines.commit_message.format_version_tag.major_minor_patch_prerelease import MajorMinorPatchPrerelease
from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.helpers.types import ROUTINE_COMMIT_MESSAGE_FORMAT_VERSION_TAG


class FormatVersionTagFactory(RoutineFactory):
    @staticmethod
    def create(routine_name: ROUTINE_COMMIT_MESSAGE_FORMAT_VERSION_TAG) -> type[FormatVersionTag]:
        return {
            RoutineFactory.skip_init(Full).factory_name(): Full,
            RoutineFactory.skip_init(FullButOnlyDigits).factory_name(): FullButOnlyDigits,
            RoutineFactory.skip_init(MajorMinorPatch).factory_name(): MajorMinorPatch,
            RoutineFactory.skip_init(MajorMinorPatchPrerelease).factory_name(): MajorMinorPatchPrerelease,
        }[routine_name]
