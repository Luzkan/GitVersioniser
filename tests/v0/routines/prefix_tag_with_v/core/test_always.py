from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.prefix_tag_with_v.routine import TestRoutinePrefixTagWithV


class TestAlways(TestRoutinePrefixTagWithV):
    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 4)),
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 3)),
        (VersionInfo(1, 2, 3), VersionInfo(1, 2, 2)),
        (VersionInfo(5, 0, 0), VersionInfo(6, 0, 0)),
        (VersionInfo(1, 1, 1), VersionInfo(0, 0, 0)),
        (VersionInfo(3, 3, 3), VersionInfo(3, 3, 3)),
    ])
    def test_true(self, old_version, new_version):
        self.routine.repo.tags.create(str(old_version))
        self.assertEqual(self.routine.run(Versions(old_version, new_version)), True)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('always')
        self.repo_utils = PseudoRepo(self.routine)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
