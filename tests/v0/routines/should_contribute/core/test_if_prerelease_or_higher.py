from unittest.mock import Mock

from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult
from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.should_contribute.routine import TestRoutineShouldContribute


class TestIfPrereleaseOrHigher(TestRoutineShouldContribute):
    @parameterized.expand([
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 2, 4)),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 3, 0)),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(2, 0, 0)),
        (SemverTag.init_spec(1, 2, 3, 'rc.1'), SemverTag.init_spec(1, 2, 3, 'rc.2')),
        (SemverTag.init_spec(1, 2, 3, 'rc.1'), SemverTag.init_spec(1, 2, 3, 'rc.3')),
        (SemverTag.init_spec(1, 2, 3, 'rc.2'), SemverTag.init_spec(1, 2, 5, 'rc.1')),
        (SemverTag.init_spec(0, 3, 2, None, None), SemverTag.init_spec(0, 3, 2, prerelease='rc.1')),
    ])
    def test_true(self, old_version, new_version):
        self.routine.repo.tags.create(str(old_version))
        self.assertEqual(self.routine.run(VersioningResult(Versions(old_version, new_version), Mock, Mock, Mock, Mock)), True)

    @parameterized.expand([
        (SemverTag.init_spec(1, 2, 3, 'rc.2'), SemverTag.init_spec(1, 2, 3, 'rc.1')),
        (SemverTag.init_spec(1, 2, 3, 'rc.4', 'build.5'), SemverTag.init_spec(0, 3, 4, 'rc.3', 'build.6')),
        (SemverTag.init_spec(0, 0, 0, 'alpha.2'), SemverTag.init_spec(0, 0, 0, 'alpha.1')),
        (SemverTag.init_spec(0, 0, 1, build='build.4'), SemverTag.init_spec(0, 0, 1, build='build.5')),
        (SemverTag.init_spec(0, 3, 2, None, None), SemverTag.init_spec(0, 3, 2, build='build.1')),
    ])
    def test_false(self, old_version, new_version):
        self.routine.repo.tags.create(str(old_version))
        self.assertEqual(self.routine.run(VersioningResult(Versions(old_version, new_version), Mock, Mock, Mock, Mock)), False)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('if_prerelease_or_higher')
        self.repo_utils = PseudoRepo(self.routine.config, self.routine.repo)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
