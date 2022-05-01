from unittest.mock import Mock

from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.helpers.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.should_contribute.routine import TestRoutineShouldContribute


class TestNever(TestRoutineShouldContribute):
    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 4)),
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 3)),
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 2)),
        (VersionInfo(5, 0, 0), VersionInfo(6, 0, 0)),
        (VersionInfo(1, 1, 1), VersionInfo(0, 0, 0)),
        (VersionInfo(3, 3, 3), VersionInfo(3, 3, 3)),
    ])
    def test_false(self, old_version, new_version):
        self.routine.repo.tags.create(str(old_version))
        self.routine.run(VersioningResult(Versions(old_version, new_version), Mock, Mock, Mock))
        self.assertEqual(self.routine.repo.tags.latest_semver, old_version)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('never')
        self.repo_utils = PseudoRepo(self.routine)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
