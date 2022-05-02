from dataclasses import dataclass
from datetime import datetime

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.changelog.abstract import RoutineChangelog
from gitversioniser.domain.versioniser.routines.changelog.core.commit_pattern.entry import ChangelogEntry
from gitversioniser.domain.versioniser.routines.changelog.utils.file import ChangelogFile


@dataclass
class CommitPattern(RoutineChangelog):
    def update_changelog(self, new_version: SemverTag, changelog: ChangelogFile) -> ChangelogFile:
        return changelog\
            .add_header([
                self._get_header(str(new_version)),
                "\n"
            ])\
            .add_entry([
                *self._get_entry()
            ])\
            .add_footer(
                self._get_footer(str(new_version), self.repo.github_user_repo, self.repo.repo_name)
            )

    @staticmethod
    def _get_header(new_version):
        return f"## [[`{new_version}`]] - {datetime.now().strftime('%Y-%m-%d')}\n"

    def _get_entry(self) -> list[str]:
        return list(self._get_entries_from_commit_messages().create_category_entries())

    @staticmethod
    def _get_footer(version: str, github_user: str, repo_name: str) -> str:
        return f"[`{version}`]: https://github.com/{github_user}/{repo_name}/releases/tag/{version}\n"

    def _get_entries_from_commit_messages(self) -> ChangelogEntry:
        changelog_changes = ChangelogEntry()
        for commit in self.repo.commits.get_commits_till_last_commit_made_by_author(self.config.credentials.username):
            if commit.summary.commit_tag.exist():
                changelog_changes.add(*commit.summary.commit_tag.get())
            else:
                changelog_changes.add_custom('Other', str(commit.summary))
        return changelog_changes

    @staticmethod
    def factory_name() -> str:
        return 'commit_pattern'
