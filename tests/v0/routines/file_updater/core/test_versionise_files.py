from pathlib import Path

from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.config.config import Config
from gitversioniser.domain.versioniser.helpers.versions import Versions
from tests.utils.temp_file import TempFile
from tests.v0.routines.file_updater.routine import TestRoutineFileUpdater


class TestVersioniseFiles(TestRoutineFileUpdater):
    def setUp(self):
        super().setUp()
        self.temp_file = TempFile()
        self.routine = self.get_routine('versionise_files')

    def tearDown(self):
        super().tearDown()
        self.temp_file.remove()

    @parameterized.expand([
        (Path('woohoo/main.py'), VersionInfo(1, 0, 0), VersionInfo(1, 0, 1)),
        (Path('README.md'), VersionInfo(1, 5, 1), VersionInfo(1, 6, 0))
    ])
    def test_by_default_no_updates_in_files(self, file_creation_path: Path, old_version: VersionInfo, new_version: VersionInfo):
        test_path: Path = self.temp_file.prepare_environment(
            Path(f"{self.config.target_repository_path}{file_creation_path}"),
            f"__version__ = '{str(old_version)}'"
        )
        self.routine.run(Versions(old=old_version, new=new_version))
        self.assertIn(str(old_version), self.temp_file.open(test_path))

    @parameterized.expand([
        (Path('woohoo/main.py'), VersionInfo(1, 0, 0), VersionInfo(1, 0, 1)),
        (Path('main/py/main.py'), VersionInfo(6, 3, 6), VersionInfo(2, 3, 4)),
        (Path('main.py'), VersionInfo(1, 1, 2), VersionInfo(1, 1, 3)),
    ])
    def test_updating_strings_in_file(self, file_creation_path: Path, old_version: VersionInfo, new_version: VersionInfo):
        self.routine.config = Config(
            target_repository_path=self.test_repo_path,
            versioned_files=[file_creation_path.name],
            routines=self.config.routines,
        )
        test_path: Path = self.temp_file.prepare_environment(
            Path(f"{self.config.target_repository_path}{file_creation_path}"),
            f"__version__ = '{str(old_version)}'"
        )
        self.routine.run(Versions(old=old_version, new=new_version))
        self.assertIn(str(new_version), self.temp_file.open(test_path))
