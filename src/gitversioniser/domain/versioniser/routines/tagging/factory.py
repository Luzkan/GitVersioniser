from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging
from gitversioniser.domain.versioniser.routines.tagging.core import Force, Never, Regular
from gitversioniser.helpers.types import ROUTINE_TAGGING_TYPE


class RoutineTaggingFactory:
    @staticmethod
    def create(routine_tagging_name: ROUTINE_TAGGING_TYPE) -> type[RoutineTagging]:
        return {
            Force.factory_name(): Force,
            Never.factory_name(): Never,
            Regular.factory_name(): Regular,
        }[routine_tagging_name]
