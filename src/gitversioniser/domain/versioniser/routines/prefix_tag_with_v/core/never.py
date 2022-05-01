from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.should_contribute.abstract import RoutineShouldContribute
from gitversioniser.domain.versioniser.utils.versions import Versions


@dataclass
class Never(RoutineShouldContribute):
    def run(self, versions: Versions) -> bool:
        return False

    @staticmethod
    def factory_name() -> str:
        return 'never'
