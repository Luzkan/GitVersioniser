from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.abstract import RoutinePrefixTagWithV
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.core import Always, IfBuildOrHigher, IfPatchOrHigher, IfPrereleaseOrHigher, Never
from gitversioniser.helpers.types import ROUTINE_PREFIX_TAG_WITH_V


class RoutinePrefixTagWithVFactory(RoutineFactory):
    @staticmethod
    def create(routine_prefix_tag_with_v: ROUTINE_PREFIX_TAG_WITH_V) -> type[RoutinePrefixTagWithV]:
        return {
            RoutineFactory.skip_init(Always).factory_name(): Always,
            RoutineFactory.skip_init(IfBuildOrHigher).factory_name(): IfBuildOrHigher,
            RoutineFactory.skip_init(IfPatchOrHigher).factory_name(): IfPatchOrHigher,
            RoutineFactory.skip_init(IfPrereleaseOrHigher).factory_name(): IfPrereleaseOrHigher,
            RoutineFactory.skip_init(Never).factory_name(): Never,
        }[routine_prefix_tag_with_v]
