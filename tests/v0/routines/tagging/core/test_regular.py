from unittest.mock import Mock

from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult
from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.tagging.routine import TestRoutineTagging


class TestRegular(TestRoutineTagging):
    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(2, 0, 0)),
        (VersionInfo(1, 2, 3), VersionInfo(1, 3, 0)),
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 4)),
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 4, 'rc.1')),
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 3, build='build.1')),
    ])
    def test_tagged(self, old_version: VersionInfo, new_version: VersionInfo):
        self.routine.repo.tags.create(str(old_version))
        self._run_routine(old_version, new_version)
        self.assertEqual(self.routine.repo.tags.latest_semver, new_version)

    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 3)),
        (VersionInfo(5, 3, 2, 'rc.2', 'build.3'), VersionInfo(5, 3, 2, 'rc.2', 'build.3')),
    ])
    def test_couldnt_tag(self, old_version, new_version):
        self.routine.repo.tags.create(str(old_version))
        self._run_routine(old_version, new_version)
        self.assertEqual(self.routine.repo.tags.latest_semver, old_version)

    def _run_routine(self, old_version, new_version):
        try:
            self.routine.run(VersioningResult(Versions(old_version, new_version), Mock, Mock, Mock, Mock))
        except ValueError as error:
            self.assertEqual(error.args[0], "Remote named 'origin' didn't exist")

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('regular')
        self.repo_utils = PseudoRepo(self.routine.config, self.routine.repo)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
