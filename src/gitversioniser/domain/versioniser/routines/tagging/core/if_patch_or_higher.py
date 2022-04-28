from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersionisingResult
from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging


@dataclass
class TagIfPatchOrHigher(RoutineTagging):
    def run(self, result: VersionisingResult):
        if any([
            result.versions.new.major > result.versions.old.major,
            result.versions.new.minor > result.versions.old.minor,
            result.versions.new.patch > result.versions.old.patch
        ]):
            return self.tag(result)

    def tag(self, result: VersionisingResult):
        self.target_repo.remote.create_tag(version=str(result.versions.new))
        self.target_repo.remote.push_tags()

    @staticmethod
    def factory_name() -> str:
        return 'if_patch_or_higher'
