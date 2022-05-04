from gitversioniser.domain.versioniser.routines.commiting.abstract import RoutineCommiting
from gitversioniser.domain.versioniser.routines.commiting.core import Null, PushOriginAmend, PushOriginNewCommit
from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.helpers.types import ROUTINE_COMMITING_TYPE


class RoutineCommitingFactory(RoutineFactory):
    @staticmethod
    def create(routine_commiting_name: ROUTINE_COMMITING_TYPE) -> type[RoutineCommiting]:
        return {
            RoutineFactory.skip_init(Null).factory_name(): Null,
            RoutineFactory.skip_init(PushOriginAmend).factory_name(): PushOriginAmend,
            RoutineFactory.skip_init(PushOriginNewCommit).factory_name(): PushOriginNewCommit,
        }[routine_commiting_name]
