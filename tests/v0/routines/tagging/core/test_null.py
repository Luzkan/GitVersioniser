from unittest.mock import Mock

from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.helpers.versions import Versions
from tests.utils.repo_utils import RepoUtils
from tests.v0.routines.tagging.routine import TestRoutineTagging


class TestNull(TestRoutineTagging):
    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 4), 'A: New Feature'),
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 2), 'F: Old Feature'),
        (VersionInfo(5, 0, 0), VersionInfo(6, 0, 0), 'R: Feature'),
        (VersionInfo(1, 1, 1), VersionInfo(0, 0, 0), 'S: The Feature'),
    ])
    def test_no_bump(self, old_version, new_version, commit_message):
        self.routine.repo.tags.create(str(old_version))
        self.routine.run(VersioningResult(Versions(old_version, new_version), commit_message, Mock, Mock))
        self.assertEqual(self.routine.repo.tags.latest_semver, old_version)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('null')
        self.repo_utils = RepoUtils(self.routine)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
