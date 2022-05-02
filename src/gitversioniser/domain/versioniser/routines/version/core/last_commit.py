from dataclasses import dataclass

from gitversioniser.domain.repository.commit import Commit
from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.version.abstract import RoutineVersion


@dataclass
class LastCommit(RoutineVersion):
    """
    Works best with:
        - Pushing to main repository branch after each commit
        - Merging develop branches to main repository branch
    """

    def generate_new_version(self) -> SemverTag:
        latest_commit: Commit = self.repo.commits.latest
        last_version: SemverTag = self.repo.tags.latest_semver
        return self._bump_version(latest_commit, last_version)

    @staticmethod
    def _bump_version(commit: Commit, version: SemverTag) -> SemverTag:
        if not commit.message.increment_tag.exist():
            return version.bump_build()
        for increment in commit.message.increment_tag.get():
            version = increment.bump_version(version)
        return version

    @staticmethod
    def factory_name() -> str:
        return 'last_commit'
