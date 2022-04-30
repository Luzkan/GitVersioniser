from unittest.mock import Mock

from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.helpers.versions import Versions
from tests.v0.routines.tagging.routine import TestRoutineTagging


class TestIfPrereleaseOrHigher(TestRoutineTagging):
    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 4), 'A: New Feature'),
        (VersionInfo(1, 2, 3), VersionInfo(1, 3, 0), 'F: Old Feature'),
        (VersionInfo(1, 2, 3), VersionInfo(2, 0, 0), 'R: Feature'),
        (VersionInfo(1, 2, 3, 'rc.1'), VersionInfo(1, 2, 3, 'rc.2'), 'R: Feature'),
        (VersionInfo(1, 2, 3, 'rc.1'), VersionInfo(1, 2, 3, 'rc.3'), 'R: Feature'),
        (VersionInfo(1, 2, 3, 'rc.2'), VersionInfo(1, 2, 5, 'rc.1'), 'R: Feature'),
        (VersionInfo(1, 2, 3, 'alpha.1'), VersionInfo(1, 2, 3, 'beta.1'), 'R: Feature'),
    ])
    def test_bump(self, old_version, new_version, commit_message):
        self.routine.target_repo.tags.create(str(old_version))
        try:
            self.routine.run(VersioningResult(Versions(old_version, new_version), commit_message, Mock, Mock))
        except ValueError as error:
            self.assertEqual(error.args[0], "Remote named 'origin' didn't exist")
            self.assertEqual(self.routine.target_repo.tags.latest_semver, new_version)

    @parameterized.expand([
        (VersionInfo(1, 2, 3, 'rc.2'), VersionInfo(1, 2, 3, 'rc.1'), 'A: New Feature'),
        (VersionInfo(1, 2, 3, 'rc.4', 'bulld.5'), VersionInfo(0, 3, 4, 'rc.5', 'build.6'), 'F: Old Feature'),
        (VersionInfo(0, 0, 0, 'alpha.2'), VersionInfo(0, 0, 0, 'alpha.1'), '[1.2.4] Trying to break thigns...'),
        (VersionInfo(0, 0, 1, build='build.4'), VersionInfo(0, 0, 1, build='build.5'), 'S: The Feature'),
    ])
    def test_no_bump(self, old_version, new_version, commit_message):
        self.routine.target_repo.tags.create(str(old_version))
        try:
            self.routine.run(VersioningResult(Versions(old_version, new_version), commit_message, Mock, Mock))
        except ValueError as error:
            self.assertEqual(error.args[0], "Remote named 'origin' didn't exist")
            self.assertEqual(self.routine.target_repo.tags.latest_semver, old_version)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('if_prerelease_or_higher')

    def tearDown(self):
        for tag in self.routine.target_repo.tags.get_sorted:
            self.routine.target_repo.repo.git.tag('-d', tag)
