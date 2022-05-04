from unittest.mock import Mock

from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult
from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.tagging.routine import TestRoutineTagging


class TestForce(TestRoutineTagging):
    @parameterized.expand([
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 2, 4)),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 2, 3)),
        (SemverTag.init_spec(1, 2, 3, 'rc.1', 'build.1'), SemverTag.init_spec(1, 2, 3, 'rc.1', 'build.1')),
    ])
    def test_tag(self, old_version: SemverTag, new_version: SemverTag):
        self.routine.repo.tags.create(str(old_version))
        self._run_routine(old_version, new_version)
        self.assertEqual(self.routine.repo.tags.latest_semver, new_version)

    def _run_routine(self, old_version, new_version):
        try:
            self.routine.run(VersioningResult(Versions(old_version, new_version), Mock, Mock, Mock, Mock))
        except ValueError as error:
            self.assertEqual(error.args[0], "Remote named 'origin' didn't exist")

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('Force')
        self.repo_utils = PseudoRepo(self.routine.config, self.routine.repo)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
