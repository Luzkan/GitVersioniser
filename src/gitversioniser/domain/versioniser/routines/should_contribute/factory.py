from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.domain.versioniser.routines.should_contribute.abstract import RoutineShouldContribute
from gitversioniser.domain.versioniser.routines.should_contribute.core import IfBuildOrHigher, IfPatchOrHigher, IfPrereleaseOrHigher, Never
from gitversioniser.helpers.types import ROUTINE_SHOULD_CONTRIBUTE


class RoutineShouldContributeFactory(RoutineFactory):
    @staticmethod
    def create(routine_should_contribute_name: ROUTINE_SHOULD_CONTRIBUTE) -> type[RoutineShouldContribute]:
        return {
            RoutineFactory.skip_init(Never).factory_name(): Never,
            RoutineFactory.skip_init(IfBuildOrHigher).factory_name(): IfBuildOrHigher,
            RoutineFactory.skip_init(IfPatchOrHigher).factory_name(): IfPatchOrHigher,
            RoutineFactory.skip_init(IfPrereleaseOrHigher).factory_name(): IfPrereleaseOrHigher,
        }[routine_should_contribute_name]
