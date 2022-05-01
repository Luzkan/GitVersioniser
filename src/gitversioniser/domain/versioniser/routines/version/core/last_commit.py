from dataclasses import dataclass

from semver import VersionInfo

from gitversioniser.domain.repository.commit import Commit
from gitversioniser.domain.versioniser.routines.version.abstract import RoutineVersion


@dataclass
class LastCommit(RoutineVersion):
    """
    Works best with:
        - Pushing to main repository branch after each commit
        - Merging develop branches to main repository branch
    """

    def generate_new_version(self) -> VersionInfo:
        latest_commit: Commit = self.repo.commits.latest
        last_version: VersionInfo = self.repo.tags.latest_semver
        return self.bump_version(latest_commit, last_version)

    def bump_version(self, commit: Commit, version: VersionInfo) -> VersionInfo:
        if not commit.message.increment_tag.exist():
            return version.bump_build()
        for increment in commit.message.increment_tag.get():
            version = increment.bump_version(version)
        return version

    @staticmethod
    def factory_name() -> str:
        return 'last_commit'
