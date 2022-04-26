from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from semver import VersionInfo

from domain.versioniser.routines.abstract import Routine
from domain.versioniser.routines.changelog.utils.file import ChangelogFile
from domain.versioniser.routines.changelog.utils.finder import ChangelogFinder


@dataclass
class RoutineChangelog(Routine, ABC):
    changelog_finder: ChangelogFinder = field(init=False, default=ChangelogFinder())

    def run(self, new_version: VersionInfo) -> None:
        self.update_changelog(new_version, ChangelogFile.init_from_path(self.changelog_finder.get_changelog())).save_file()

    @abstractmethod
    def update_changelog(self, new_version: VersionInfo, changelog_file: ChangelogFile) -> ChangelogFile:
        """ Must return updated changelog."""
