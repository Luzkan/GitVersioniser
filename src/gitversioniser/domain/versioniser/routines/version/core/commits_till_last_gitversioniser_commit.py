from dataclasses import dataclass

from semver import VersionInfo

from gitversioniser.domain.repository.commit import Commit
from gitversioniser.domain.versioniser.routines.version.abstract import RoutineVersion


@dataclass
class CommitsTillLastGitVersioniserCommits(RoutineVersion):
    """
    Works best with:
        - Pushing to main repository branch with multiple commits
        - Merging develop branches to main repository branch
    """

    def generate_new_version(self) -> VersionInfo:
        last_version: VersionInfo = self.repo.tags.latest_semver
        for commit in self.repo.commits.get_commits_till_last_commit_made_by_author(self.config.credentials.username):
            last_version: VersionInfo = self.bump_version(commit, last_version)  # type: ignore [no-redef]
        return last_version

    def bump_version(self, commit: Commit, version: VersionInfo) -> VersionInfo:
        if not commit.message.bump_tag.exist():
            return version.bump_build()
        return self.default_bump_mapping(version)[commit.message.bump_tag.get()]()

    @staticmethod
    def factory_name() -> str:
        return 'commits_till_last_gitversioniser_commit'
