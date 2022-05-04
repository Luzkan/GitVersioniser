from dataclasses import dataclass

from gitversioniser.domain.repository.commit import Commit
from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.version.abstract import RoutineVersion


@dataclass
class CommitsTillLastGitVersioniserCommit(RoutineVersion):
    """
    Works best with:
        - Pushing to main repository branch with multiple commits
        - Merging develop branches to main repository branch
    """

    def generate_new_version(self) -> SemverTag:
        last_version: SemverTag = self.repo.tags.latest_semver
        for commit in self.repo.commits.get_commits_till_last_commit_made_by_author(self.config.credentials.username):
            last_version = self._bump_version(commit, last_version)
        return last_version

    @staticmethod
    def _bump_version(commit: Commit, version: SemverTag) -> SemverTag:
        if not commit.message.increment_tag.exist():
            return version.bump_build()
        for increment in commit.message.increment_tag.get():
            version = increment.bump_version(version)
        return version
