from gitversioniser.domain.versioniser.routines.commiting.abstract import RoutineCommiting
from gitversioniser.domain.versioniser.routines.commiting.core import Null, PushOriginAmend, PushOriginNewCommit
from gitversioniser.helpers.types import ROUTINE_COMMITING_TYPE


class RoutineCommitingFactory:
    @staticmethod
    def create(routine_commiting_name: ROUTINE_COMMITING_TYPE) -> type[RoutineCommiting]:
        return {
            Null.factory_name(): Null,
            PushOriginAmend.factory_name(): PushOriginAmend,
            PushOriginNewCommit.factory_name(): PushOriginNewCommit,
        }[routine_commiting_name]
