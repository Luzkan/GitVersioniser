from gitversioniser.domain.versioniser.routines.commiting.abstract import RoutineCommiting
from gitversioniser.domain.versioniser.routines.commiting.core import Null, PushMainAmend, PushMainNewCommit
from gitversioniser.helpers.types import ROUTINE_COMMITING_TYPE


class RoutineCommitingFactory:
    @staticmethod
    def create(routine_commiting_name: ROUTINE_COMMITING_TYPE) -> type[RoutineCommiting]:
        return {
            Null.factory_name(): Null,
            PushMainAmend.factory_name(): PushMainAmend,
            PushMainNewCommit.factory_name(): PushMainNewCommit,
        }[routine_commiting_name]
