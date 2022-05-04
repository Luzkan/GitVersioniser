from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.abstract import RoutinePrefixTagWithV
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.core import (
    Always,
    IfNewVersionIsBuildOrHigher,
    IfNewVersionIsPatchOrHigher,
    IfNewVersionIsPrereleaseOrHigher,
    Never,
)
from gitversioniser.helpers.types import ROUTINE_PREFIX_TAG_WITH_V


class RoutinePrefixTagWithVFactory(RoutineFactory):
    @staticmethod
    def create(routine_prefix_tag_with_v: ROUTINE_PREFIX_TAG_WITH_V) -> type[RoutinePrefixTagWithV]:
        return {
            RoutineFactory.skip_init(Always).factory_name(): Always,
            RoutineFactory.skip_init(IfNewVersionIsBuildOrHigher).factory_name(): IfNewVersionIsBuildOrHigher,
            RoutineFactory.skip_init(IfNewVersionIsPatchOrHigher).factory_name(): IfNewVersionIsPatchOrHigher,
            RoutineFactory.skip_init(IfNewVersionIsPrereleaseOrHigher).factory_name(): IfNewVersionIsPrereleaseOrHigher,
            RoutineFactory.skip_init(Never).factory_name(): Never,
        }[routine_prefix_tag_with_v]
