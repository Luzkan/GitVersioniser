from dataclasses import dataclass
from datetime import datetime

from semver import VersionInfo

from gitversioniser.domain.versioniser.routines.changelog.abstract import RoutineChangelog
from gitversioniser.domain.versioniser.routines.changelog.core.commit_pattern.entry import ChangelogEntry
from gitversioniser.domain.versioniser.routines.changelog.utils.file import ChangelogFile


@dataclass
class CommitPattern(RoutineChangelog):
    def update_changelog(self, new_version: VersionInfo, changelog: ChangelogFile) -> ChangelogFile:
        return changelog\
            .add_header([
                self.get_header(str(new_version)),
                "\n"
            ])\
            .add_entry([
                *self.get_entry()
            ])\
            .add_footer(
                self.get_footer(str(new_version), self.target_repo.github_user_repo, self.target_repo.repo_name)
            )

    def get_header(self, new_version):
        return f"## [[`{new_version}`]] - {datetime.now().strftime('%Y-%m-%d')}\n"

    def get_entry(self) -> list[str]:
        return list(self.get_entries_from_commit_messages().create_category_entries())

    def get_footer(self, version: str, github_user: str, repo_name: str) -> str:
        return f"[`{version}`]: https://github.com/{github_user}/{repo_name}/releases/tag/{version}\n"

    def get_entries_from_commit_messages(self) -> ChangelogEntry:
        changelog_changes = ChangelogEntry()
        for commit in self.target_repo.commits.get_commits_till_last_commit_made_by_author(self.config.credentials.username):
            if commit.summary.commit_tag.exist():
                changelog_changes.add(*commit.summary.commit_tag.get())
            else:
                changelog_changes.add_custom('Other', str(commit.summary))
        return changelog_changes

    @staticmethod
    def factory_name() -> str:
        return 'commit_pattern'
