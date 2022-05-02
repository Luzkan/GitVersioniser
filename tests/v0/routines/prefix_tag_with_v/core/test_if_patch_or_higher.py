from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.prefix_tag_with_v.routine import TestRoutinePrefixTagWithV


class TestIfPatchOrHigher(TestRoutinePrefixTagWithV):
    @parameterized.expand([
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 2, 4)),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 3, 0)),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(2, 0, 0)),
    ])
    def test_true(self, old_version: SemverTag, new_version: SemverTag):
        self.routine.repo.tags.create(str(old_version))
        self.assertEqual(self.routine.run(Versions(old_version, new_version)), True)

    @parameterized.expand([
        (SemverTag.init_spec(2, 0, 0, 'rc.1'), SemverTag.init_spec(2, 0, 0, 'rc.2')),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 2, 3, 'build.1')),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 2, 2)),
        (SemverTag.init_spec(0, 0, 1, build='build.4'), SemverTag.init_spec(0, 0, 1, build='build.5')),
    ])
    def test_false(self, old_version: SemverTag, new_version: SemverTag):
        self.routine.repo.tags.create(str(old_version))
        self.assertEqual(self.routine.run(Versions(old_version, new_version)), False)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('if_patch_or_higher')
        self.repo_utils = PseudoRepo(self.routine.config, self.routine.repo)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
