from unittest.mock import Mock

from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.helpers.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.should_contribute.routine import TestRoutineShouldContribute


class TestAlways(TestRoutineShouldContribute):
    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 4)),
        (VersionInfo(5, 0, 0), VersionInfo(6, 0, 0)),
    ])
    def test_true(self, old_version, new_version):
        self.routine.repo.tags.create(str(old_version))
        self.assertEqual(self.routine.run(VersioningResult(Versions(old_version, new_version), Mock, Mock, Mock)), True)

    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 2)),
        (VersionInfo(1, 1, 1), VersionInfo(0, 0, 0)),
    ])
    def test_false(self, old_version, new_version):
        self.routine.repo.tags.create(str(old_version))
        self.assertEqual(self.routine.run(VersioningResult(Versions(old_version, new_version), Mock, Mock, Mock)), False)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('if_build_or_higher')
        self.repo_utils = PseudoRepo(self.routine)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
