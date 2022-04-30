from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging


@dataclass
class Always(RoutineTagging):
    def run(self, result: VersioningResult):
        self.repo.remote.create_tag(version=str(result.versions.new))
        self.repo.remote.push_tags()

    @staticmethod
    def factory_name() -> str:
        return 'always'
