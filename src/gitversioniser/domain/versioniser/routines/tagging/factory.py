from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging
from gitversioniser.domain.versioniser.routines.tagging.core import Force, Never, Regular
from gitversioniser.helpers.types import ROUTINE_TAGGING_TYPE


class RoutineTaggingFactory(RoutineFactory):
    @staticmethod
    def create(routine_tagging_name: ROUTINE_TAGGING_TYPE) -> type[RoutineTagging]:
        return {
            RoutineFactory.skip_init(Force).factory_name(): Force,
            RoutineFactory.skip_init(Never).factory_name(): Never,
            RoutineFactory.skip_init(Regular).factory_name(): Regular,
        }[routine_tagging_name]
