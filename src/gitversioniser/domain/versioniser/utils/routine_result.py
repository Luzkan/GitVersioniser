from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.changelog.utils.file import ChangelogFile
from gitversioniser.domain.versioniser.routines.file_updater.utils.updated_files import UpdatedFiles
from gitversioniser.domain.versioniser.utils.versions import Versions
from gitversioniser.helpers.logger import CONSOLE


@dataclass(frozen=True)
class VersioningResult:
    versions: Versions
    commit_message: str
    prefix_tag_with_v: bool
    updated_files: UpdatedFiles
    changelog: ChangelogFile

    def __post_init__(self):
        CONSOLE.rule('Versioning Result')
        CONSOLE.print(self)
