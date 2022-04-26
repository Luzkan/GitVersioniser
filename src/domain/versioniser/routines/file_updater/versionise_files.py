from dataclasses import dataclass
from pathlib import Path

from domain.versioniser.routines.file_updater.abstract import RoutineFileUpdater
from domain.versioniser.routines.version.utils.versions import Versions


@dataclass
class VersioniseFiles(RoutineFileUpdater):
    def run(self, versions: Versions) -> None:
        self.replace_version_strings_in_versionised_files(versions)

    def replace_version_strings_in_versionised_files(self, versions):
        for filename in self.config.versioned_files:
            self.replace_version(self.find_file(filename), versions)

    def find_file(self, filename: str) -> Path:
        return sorted(Path('.').glob(f'**/{filename}'))[0]

    def replace_version(self, filepath: Path, versions: Versions) -> None:
        with filepath.open('r') as file:
            content = file.read()

        with filepath.open('w') as file:
            file.write(content.replace(str(versions.old), str(versions.new)))

    @staticmethod
    def factory_name() -> str:
        return 'versionise_files'
