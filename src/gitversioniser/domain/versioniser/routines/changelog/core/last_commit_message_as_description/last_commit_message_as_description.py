from dataclasses import dataclass
from datetime import datetime

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.changelog.abstract import RoutineChangelog
from gitversioniser.domain.versioniser.routines.changelog.utils.file import ChangelogFile


@dataclass
class LastCommitMessageAsDescription(RoutineChangelog):
    def update_changelog(self, new_version: SemverTag, changelog: ChangelogFile) -> ChangelogFile:
        return changelog\
            .add_header([
                self._get_header(str(new_version)),
                "\n",
                self._get_description(),
                "\n"
            ])\
            .add_footer(
                self._get_footer(str(new_version), self.repo.github_user_repo, self.repo.repo_name)
            )

    @staticmethod
    def _get_header(new_version: str) -> str:
        return f"## [[`{new_version}`]] - {datetime.now().strftime('%Y-%m-%d')}\n"

    def _get_description(self) -> str:
        return f"{self.repo.commits.latest.message.value}\n"

    @staticmethod
    def _get_footer(version: str, github_user: str, repo_name: str) -> str:
        return f"[`{version}`]: https://github.com/{github_user}/{repo_name}/releases/tag/{version}\n"

    @staticmethod
    def factory_name() -> str:
        return 'last_commit_message_as_description'
