from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging


@dataclass
class IfPatchOrHigher(RoutineTagging):
    def run(self, result: VersioningResult):
        if any([
            result.versions.new.major > result.versions.old.major,
            result.versions.new.minor > result.versions.old.minor,
            result.versions.new.patch > result.versions.old.patch
        ]):
            return self.tag(result)

    def tag(self, result: VersioningResult):
        self.repo.remote.create_tag(version=str(result.versions.new))
        self.repo.remote.push_tags()

    @staticmethod
    def factory_name() -> str:
        return 'if_patch_or_higher'
