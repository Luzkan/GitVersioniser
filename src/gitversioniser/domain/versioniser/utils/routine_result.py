from dataclasses import dataclass

from rich import print

from gitversioniser.domain.versioniser.routines.changelog.utils.file import ChangelogFile
from gitversioniser.domain.versioniser.routines.file_updater.utils.updated_files import UpdatedFiles
from gitversioniser.domain.versioniser.utils.versions import Versions


@dataclass(frozen=True)
class VersioningResult:
    versions: Versions
    commit_message: str
    updated_files: UpdatedFiles
    changelog: ChangelogFile
    prefix_tag_with_v: bool

    def __post_init__(self):
        print(self)