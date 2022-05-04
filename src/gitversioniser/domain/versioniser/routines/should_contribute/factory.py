from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.domain.versioniser.routines.should_contribute.abstract import RoutineShouldContribute
from gitversioniser.domain.versioniser.routines.should_contribute.core import (
    IfNewVersionIsBuildOrHigher,
    IfNewVersionIsPatchOrHigher,
    IfNewVersionIsPrereleaseOrHigher,
    Never,
)
from gitversioniser.helpers.types import ROUTINE_SHOULD_CONTRIBUTE


class RoutineShouldContributeFactory(RoutineFactory):
    @staticmethod
    def create(routine_should_contribute_name: ROUTINE_SHOULD_CONTRIBUTE) -> type[RoutineShouldContribute]:
        return {
            RoutineFactory.skip_init(Never).factory_name(): Never,
            RoutineFactory.skip_init(IfNewVersionIsBuildOrHigher).factory_name(): IfNewVersionIsBuildOrHigher,
            RoutineFactory.skip_init(IfNewVersionIsPatchOrHigher).factory_name(): IfNewVersionIsPatchOrHigher,
            RoutineFactory.skip_init(IfNewVersionIsPrereleaseOrHigher).factory_name(): IfNewVersionIsPrereleaseOrHigher,
        }[routine_should_contribute_name]
