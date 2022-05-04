from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.abstract import RoutinePrefixTagWithV
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass
class Never(RoutinePrefixTagWithV):
    def run(self, result: VersioningResult) -> bool:
        return False
