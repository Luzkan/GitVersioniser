from unittest.mock import Mock

from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.helpers.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.should_contribute.routine import TestRoutineShouldContribute


class TestIfPrereleaseOrHigher(TestRoutineShouldContribute):
    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 4)),
        (VersionInfo(1, 2, 3), VersionInfo(1, 3, 0)),
        (VersionInfo(1, 2, 3), VersionInfo(2, 0, 0)),
        (VersionInfo(1, 2, 3, 'rc.1'), VersionInfo(1, 2, 3, 'rc.2')),
        (VersionInfo(1, 2, 3, 'rc.1'), VersionInfo(1, 2, 3, 'rc.3')),
        (VersionInfo(1, 2, 3, 'rc.2'), VersionInfo(1, 2, 5, 'rc.1')),
    ])
    def test_true(self, old_version, new_version):
        self.routine.repo.tags.create(str(old_version))
        self.assertEqual(self.routine.run(VersioningResult(Versions(old_version, new_version), Mock, Mock, Mock)), True)

    @parameterized.expand([
        (VersionInfo(1, 2, 3, 'rc.2'), VersionInfo(1, 2, 3, 'rc.1')),
        (VersionInfo(1, 2, 3, 'rc.4', 'build.5'), VersionInfo(0, 3, 4, 'rc.3', 'build.6')),
        (VersionInfo(0, 0, 0, 'alpha.2'), VersionInfo(0, 0, 0, 'alpha.1')),
        (VersionInfo(0, 0, 1, build='build.4'), VersionInfo(0, 0, 1, build='build.5')),
    ])
    def test_false(self, old_version, new_version):
        self.routine.repo.tags.create(str(old_version))
        self.assertEqual(self.routine.run(VersioningResult(Versions(old_version, new_version), Mock, Mock, Mock)), False)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('if_prerelease_or_higher')
        self.repo_utils = PseudoRepo(self.routine)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
