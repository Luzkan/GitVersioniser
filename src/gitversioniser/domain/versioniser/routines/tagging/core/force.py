from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass
class Force(RoutineTagging):
    def run(self, result: VersioningResult) -> None:
        self.repo.remote.create_tag(version=result.versions.new.to_string(with_prefix_v=result.prefix_tag_with_v))
        self.repo.remote.push_tags_force()
