from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.routines.should_contribute.abstract import RoutineShouldContribute
from gitversioniser.domain.versioniser.routines.should_contribute.utils.version_comparer import VersionComparer


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

    @staticmethod
    def factory_name() -> str:
        return 'if_build_or_higher'
