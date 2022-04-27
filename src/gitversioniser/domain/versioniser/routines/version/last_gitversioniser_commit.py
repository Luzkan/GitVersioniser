from dataclasses import dataclass

from semver import VersionInfo

from gitversioniser.domain.repository.commit import Commit
from gitversioniser.domain.versioniser.routines.version.abstract import RoutineVersion


@dataclass
class LastGitVersioniserCommit(RoutineVersion):
    """
    Increments the version based on commit messages up until last commit made by GitVersioniser.

    Works best with:
        - Pushing to main repository branch with multiple commits
        - Merging develop branches to main repository branch
    """

    def generate_new_version(self) -> VersionInfo:
        last_version: VersionInfo = self.target_repo.tags.latest_semver
        for commit in self.target_repo.commits.get_commits_till_last_commit_made_by_author(self.config.credentials.username):
            last_version: VersionInfo = self.bump_version(commit, last_version)  # type: ignore [no-redef]
        return last_version

    def bump_version(self, commit: Commit, version: VersionInfo) -> VersionInfo:
        if not commit.summary.bump_tag.exist():
            return version.bump_build()
        return self.default_bump_mapping(version)[commit.summary.bump_tag.get()]()

    @staticmethod
    def factory_name() -> str:
        return 'last_gitversioniser_commit'
