from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.helpers.routine_result import VersionisingResult
from gitversioniser.domain.versioniser.routines.version.utils.versions import Versions
from tests.v0.routines.tagging.routine import TestRoutineTagging


class TestIfPatchOrHigher(TestRoutineTagging):
    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 4), 'A: New Feature'),
        (VersionInfo(1, 2, 3), VersionInfo(1, 3, 0), 'F: Old Feature'),
        (VersionInfo(1, 2, 3), VersionInfo(2, 0, 0), 'R: Feature'),
    ])
    def test_bump(self, old_version, new_version, commit_message):
        self.routine.target_repo.tags.create(str(old_version))
        try:
            self.routine.run(VersionisingResult(Versions(old_version, new_version), commit_message))
        except ValueError as error:
            self.assertEqual(error.args[0], "Remote named 'origin' didn't exist")
            self.assertEqual(self.routine.target_repo.tags.latest_semver, new_version)

    @parameterized.expand([
        (VersionInfo(2, 0, 0, 'rc.1'), VersionInfo(2, 0, 0, 'rc.2'), 'A: New Feature'),
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 3, 'build.1'), 'F: Old Feature'),
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 2), '[1.2.4] Trying to break thigns...'),
        (VersionInfo(0, 0, 1, build='build.4'), VersionInfo(0, 0, 1, build='build.5'), 'S: The Feature'),
    ])
    def test_no_bump(self, old_version, new_version, commit_message):
        self.routine.target_repo.tags.create(str(old_version))
        try:
            self.routine.run(VersionisingResult(Versions(old_version, new_version), commit_message))
        except ValueError as error:
            self.assertEqual(error.args[0], "Remote named 'origin' didn't exist")
            self.assertEqual(self.routine.target_repo.tags.latest_semver, old_version)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('if_patch_or_higher')

    def tearDown(self):
        for tag in self.routine.target_repo.tags.get_sorted:
            self.routine.target_repo.repo.git.tag('-d', tag)
