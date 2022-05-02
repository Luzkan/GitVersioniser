from unittest.mock import Mock

from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult
from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.should_contribute.routine import TestRoutineShouldContribute


class TestNever(TestRoutineShouldContribute):
    @parameterized.expand([
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 2, 4)),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 2, 3)),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 2, 2)),
        (SemverTag.init_spec(5, 0, 0), SemverTag.init_spec(6, 0, 0)),
        (SemverTag.init_spec(1, 1, 1), SemverTag.init_spec(0, 0, 0)),
        (SemverTag.init_spec(3, 3, 3), SemverTag.init_spec(3, 3, 3)),
    ])
    def test_false(self, old_version, new_version):
        self.routine.repo.tags.create(str(old_version))
        self.routine.run(VersioningResult(Versions(old_version, new_version), Mock, Mock, Mock, Mock))
        self.assertEqual(self.routine.repo.tags.latest_semver, old_version)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('never')
        self.repo_utils = PseudoRepo(self.routine.config, self.routine.repo)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
