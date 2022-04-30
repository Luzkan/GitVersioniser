from dataclasses import dataclass
from pathlib import Path

from gitversioniser.domain.versioniser.helpers.versions import Versions
from gitversioniser.domain.versioniser.routines.file_updater.abstract import RoutineFileUpdater
from gitversioniser.domain.versioniser.routines.file_updater.utils.updated_files import UpdatedFiles


@dataclass
class VersioniseFiles(RoutineFileUpdater):
    def run(self, versions: Versions) -> UpdatedFiles:
        return UpdatedFiles.init_normalize([self.replace_version(self.find_file(filename), versions) for filename in self.config.versioned_files])

    def find_file(self, filename: str) -> Path:
        return sorted(Path(self.config.target_repository_path).glob(f'**/{filename}'))[0]

    def replace_version(self, filepath: Path, versions: Versions) -> Path | None:
        with filepath.open('r') as file:
            old_content = file.read()

        with filepath.open('w') as file:
            file.write(old_content.replace(str(versions.old), str(versions.new)))

        return filepath if str(versions.old) in old_content else None

    @staticmethod
    def factory_name() -> str:
        return 'versionise_files'
