from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.domain.versioniser.routines.changelog.utils.file import ChangelogFile
from gitversioniser.domain.versioniser.routines.changelog.utils.finder import ChangelogFinder


@dataclass  # type: ignore [misc]
class RoutineChangelog(Routine, ABC):
    changelog_finder: ChangelogFinder = field(init=False, default=ChangelogFinder())

    def run(self, new_version: SemverTag) -> ChangelogFile:
        return self.update_changelog(new_version, ChangelogFile.init_from_path(self.changelog_finder.get_changelog())).save_file()

    @abstractmethod
    def update_changelog(self, new_version: SemverTag, changelog: ChangelogFile) -> ChangelogFile:
        """ Must return updated changelog."""
