from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.version_comparer import VersionComparer
from gitversioniser.domain.versioniser.routines.should_contribute.abstract import RoutineShouldContribute
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass
class IfBuildOrHigher(RoutineShouldContribute):
    def run(self, result: VersioningResult) -> bool:
        version_comparer = VersionComparer(result.versions)
        return any([
            version_comparer.is_new_major(),
            version_comparer.is_new_minor(),
            version_comparer.is_new_patch(),
            version_comparer.is_new_prerelease(),
            version_comparer.is_new_build()
        ])
