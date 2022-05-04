from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass
class Regular(RoutineTagging):
    def run(self, result: VersioningResult):
        self.repo.remote.create_tag(version=self._create_tag_string(result))
        self.repo.remote.push_tags()

    @staticmethod
    def _create_tag_string(result: VersioningResult) -> str:
        return f"v{str(result.versions.new)}" if result.prefix_tag_with_v else str(result.versions.new)
