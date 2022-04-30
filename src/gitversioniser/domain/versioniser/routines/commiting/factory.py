from gitversioniser.domain.versioniser.routines.commiting.abstract import RoutineCommiting
from gitversioniser.domain.versioniser.routines.commiting.core import Null, PushMainAmend, PushMainNew
from gitversioniser.helpers.types import ROUTINE_COMMITING_TYPE


class RoutineCommitingFactory:
    @staticmethod
    def create(routine_commiting_name: ROUTINE_COMMITING_TYPE) -> type[RoutineCommiting]:
        return {
            Null.factory_name(): Null,
            PushMainAmend.factory_name(): PushMainAmend,
            PushMainNew.factory_name(): PushMainNew,
        }[routine_commiting_name]
