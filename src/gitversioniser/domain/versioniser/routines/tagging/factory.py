from gitversioniser.domain.versioniser.routines.contribution.core.null import Null
from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging
from gitversioniser.domain.versioniser.routines.tagging.core.always import Always
from gitversioniser.domain.versioniser.routines.tagging.core.if_patch_or_higher import TagIfPatchOrHigher
from gitversioniser.domain.versioniser.routines.tagging.core.if_prerelease_or_higher import TagIfPrereleaseOrHigher
from gitversioniser.helpers.types import ROUTINE_TAGGING_TYPE


class RoutineTaggingFactory:
    @staticmethod
    def create(routine_tagging_name: ROUTINE_TAGGING_TYPE) -> type[RoutineTagging]:
        return {
            Null.factory_name(): Null,
            Always.factory_name(): Always,
            TagIfPatchOrHigher.factory_name(): TagIfPatchOrHigher,
            TagIfPrereleaseOrHigher.factory_name(): TagIfPrereleaseOrHigher,
        }[routine_tagging_name]
