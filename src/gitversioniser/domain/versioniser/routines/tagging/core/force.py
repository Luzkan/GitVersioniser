from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass
class Force(RoutineTagging):
    def run(self, result: VersioningResult):
        self.repo.remote.create_tag(version=self.create_tag_string(result))
        self.repo.remote.push_tags_force()

    def create_tag_string(self, result: VersioningResult) -> str:
        return f"v{str(result.versions.new)}" if result.prefix_tag_with_v else str(result.versions.new)

    @staticmethod
    def factory_name() -> str:
        return 'force'
