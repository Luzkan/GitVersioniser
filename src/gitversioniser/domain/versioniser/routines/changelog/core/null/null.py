from dataclasses import dataclass
from pathlib import Path

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.changelog.abstract import RoutineChangelog
from gitversioniser.domain.versioniser.routines.changelog.utils.file import ChangelogFile


@dataclass
class Null(RoutineChangelog):
    def run(self, new_version: SemverTag) -> ChangelogFile:
        """ This routine does nothing. """
        return ChangelogFile(Path(''), list())

    def update_changelog(self, new_version: SemverTag, changelog: ChangelogFile) -> ChangelogFile:
        return ChangelogFile(Path(''), list())
