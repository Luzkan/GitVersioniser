from gitversioniser.domain.versioniser.routines.should_contribute.abstract import RoutineShouldContribute
from gitversioniser.domain.versioniser.routines.should_contribute.core import IfBuildOrHigher, IfPatchOrHigher, IfPrereleaseOrHigher, Never
from gitversioniser.helpers.types import ROUTINE_SHOULD_CONTRIBUTE


class RoutineShouldContributeFactory:
    @staticmethod
    def create(routine_should_contribute_name: ROUTINE_SHOULD_CONTRIBUTE) -> type[RoutineShouldContribute]:
        return {
            Never.factory_name(): Never,
            IfBuildOrHigher.factory_name(): IfBuildOrHigher,
            IfPatchOrHigher.factory_name(): IfPatchOrHigher,
            IfPrereleaseOrHigher.factory_name(): IfPrereleaseOrHigher,
        }[routine_should_contribute_name]
