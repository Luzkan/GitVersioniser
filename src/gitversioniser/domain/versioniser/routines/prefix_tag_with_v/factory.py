from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.abstract import RoutinePrefixTagWithV
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.core import Always, IfBuildOrHigher, IfPatchOrHigher, IfPrereleaseOrHigher, Never
from gitversioniser.helpers.types import ROUTINE_PREFIX_TAG_WITH_V


class RoutinePrefixTagWithVFactory:
    @staticmethod
    def create(routine_prefix_tag_with_v: ROUTINE_PREFIX_TAG_WITH_V) -> type[RoutinePrefixTagWithV]:
        return {
            Always.factory_name(): Always,
            IfBuildOrHigher.factory_name(): IfBuildOrHigher,
            IfPatchOrHigher.factory_name(): IfPatchOrHigher,
            IfPrereleaseOrHigher.factory_name(): IfPrereleaseOrHigher,
            Never.factory_name(): Never,
        }[routine_prefix_tag_with_v]
