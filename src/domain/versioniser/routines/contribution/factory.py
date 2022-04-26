from domain.versioniser.routines.contribution.abstract import RoutineContribution
from domain.versioniser.routines.contribution.null import Null
from domain.versioniser.routines.contribution.push_main_amend import PushMainAmend
from domain.versioniser.routines.contribution.push_main_new import PushMainNew
from helpers.types import ROUTINE_CONTRIBUTION_TYPE


class RoutineContributionFactory:
    @staticmethod
    def create(routine_contribution_name: ROUTINE_CONTRIBUTION_TYPE) -> type[RoutineContribution]:
        return {
            Null.factory_name(): Null,
            PushMainAmend.factory_name(): PushMainAmend,
            PushMainNew.factory_name(): PushMainNew,
        }[routine_contribution_name]
