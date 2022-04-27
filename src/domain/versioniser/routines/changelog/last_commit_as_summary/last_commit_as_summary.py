from dataclasses import dataclass
from datetime import datetime

from semver import VersionInfo

from domain.versioniser.routines.changelog.abstract import RoutineChangelog
from domain.versioniser.routines.changelog.utils.file import ChangelogFile


@dataclass
class LastCommitAsSummary(RoutineChangelog):
    def update_changelog(self, new_version: VersionInfo, changelog: ChangelogFile) -> ChangelogFile:
        return changelog\
            .add_header([
                self.get_header(str(new_version)),
                "\n",
                self.get_description(),
                "\n"
            ])

    def get_header(self, new_version) -> str:
        return f"## [{new_version}] - {datetime.now().strftime('%Y-%m-%d')}\n"

    def get_description(self) -> str:
        return f"{self.target_repo.commits.latest.summary}\n"

    @staticmethod
    def factory_name() -> str:
        return 'last_commit_as_summary'
