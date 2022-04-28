from gitversioniser.domain.versioniser.routines.contribution.abstract import RoutineContribution
from gitversioniser.domain.versioniser.routines.contribution.core.null import Null
from gitversioniser.domain.versioniser.routines.contribution.core.push_main_amend import PushMainAmend
from gitversioniser.domain.versioniser.routines.contribution.core.push_main_new import PushMainNew
from gitversioniser.helpers.types import ROUTINE_CONTRIBUTION_TYPE


class RoutineContributionFactory:
    @staticmethod
    def create(routine_contribution_name: ROUTINE_CONTRIBUTION_TYPE) -> type[RoutineContribution]:
        return {
            Null.factory_name(): Null,
            PushMainAmend.factory_name(): PushMainAmend,
            PushMainNew.factory_name(): PushMainNew,
        }[routine_contribution_name]
