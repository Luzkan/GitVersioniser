from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.helpers.routine_result import VersionisingResult
from gitversioniser.domain.versioniser.routines.version.utils.versions import Versions
from tests.v0.routines.tagging.routine import TestRoutineTagging


class TestNull(TestRoutineTagging):
    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 4), 'A: New Feature'),
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 2), 'F: Old Feature'),
        (VersionInfo(5, 0, 0), VersionInfo(6, 0, 0), 'R: Feature'),
        (VersionInfo(1, 1, 1), VersionInfo(0, 0, 0), 'S: The Feature'),
    ])
    def test_no_bump(self, old_version, new_version, commit_message):
        self.routine.target_repo.tags.create(str(old_version))
        self.routine.run(VersionisingResult(Versions(old_version, new_version), commit_message))
        self.assertEqual(self.routine.target_repo.tags.latest_semver, old_version)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('null')

    def tearDown(self):
        for tag in self.routine.target_repo.tags.get_sorted:
            self.routine.target_repo.repo.git.tag('-d', tag)
