from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.routines.tagging.abstract import RoutineTagging
from gitversioniser.helpers.regex_pattern import RegexPattern


@dataclass
class IfPrereleaseOrHigher(RoutineTagging):
    def run(self, result: VersioningResult):
        if any([
            result.versions.new.major > result.versions.old.major,
            result.versions.new.minor > result.versions.old.minor,
            result.versions.new.patch > result.versions.old.patch,
            self.prerelease_number(result.versions.new.prerelease) > self.prerelease_number(result.versions.old.prerelease),
        ]):
            return self.tag(result)

    def prerelease_number(self, prerelease: str | None) -> int:
        if not prerelease:
            return 0
        match = RegexPattern.prerelease(prerelease)
        return int(match.group(1)) if match else 0

    def tag(self, result: VersioningResult):
        self.repo.remote.create_tag(version=str(result.versions.new))
        self.repo.remote.push_tags()

    @staticmethod
    def factory_name() -> str:
        return 'if_prerelease_or_higher'
