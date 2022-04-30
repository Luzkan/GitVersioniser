from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging
from gitversioniser.domain.versioniser.routines.tagging.core import Always, IfPatchOrHigher, IfPrereleaseOrHigher, Null
from gitversioniser.helpers.types import ROUTINE_TAGGING_TYPE


class RoutineTaggingFactory:
    @staticmethod
    def create(routine_tagging_name: ROUTINE_TAGGING_TYPE) -> type[RoutineTagging]:
        return {
            Null.factory_name(): Null,
            Always.factory_name(): Always,
            IfPatchOrHigher.factory_name(): IfPatchOrHigher,
            IfPrereleaseOrHigher.factory_name(): IfPrereleaseOrHigher,
        }[routine_tagging_name]
