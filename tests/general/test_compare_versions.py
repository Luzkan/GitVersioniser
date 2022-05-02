from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from tests.general.general_scenario import TestGeneralScenario
from tests.utils.pseudo_repo import PseudoRepo


class TestCompareVersions(TestGeneralScenario):
    @parameterized.expand([
        (SemverTag.init('v1.0.0'), SemverTag.init('v1.0.0+build.1')),                           # build
        (SemverTag.init('v1.0.0+build.1'), SemverTag.init('v1.0.0+build.2')),                   # build
        (SemverTag.init('v1.0.0+build.2'), SemverTag.init('v1.0.1')),                           # patch
        (SemverTag.init('v1.0.1'), SemverTag.init('v1.0.2')),                                   # patch
        (SemverTag.init('v1.0.2'), SemverTag.init('v1.1.0')),                                   # minor
        (SemverTag.init('v1.1.0'), SemverTag.init('v2.0.0')),                                   # major
        (SemverTag.init('v2.0.0'), SemverTag.init('v3.0.0-alpha.1')),                           # alpha
        (SemverTag.init('v3.0.0-alpha.1'), SemverTag.init('v3.0.0-alpha.2')),                   # alpha
        (SemverTag.init('v3.0.0-alpha.2'), SemverTag.init('v3.0.0-alpha.2+build.1')),           # build
        (SemverTag.init('v3.0.0-alpha.2+build.1'), SemverTag.init('v3.0.0-alpha.2+build.2')),   # build
        (SemverTag.init('v3.0.0-alpha.2+build.2'), SemverTag.init('v3.0.0-beta.1')),            # beta
        (SemverTag.init('v3.0.0-beta.1'), SemverTag.init('v3.0.0-beta.1+build.1')),             # build
        (SemverTag.init('v3.0.0-beta.1+build.1'), SemverTag.init('v3.0.0-beta.2')),             # beta
        (SemverTag.init('v3.0.0-beta.2'), SemverTag.init('v3.0.0-rc.1')),                       # rc
        (SemverTag.init('v3.0.0-rc.1'), SemverTag.init('v3.0.0-rc.2')),                         # rc
        (SemverTag.init('v3.0.0-rc.2'), SemverTag.init('v3.0.0')),                              # final
        (SemverTag.init('v3.0.0'), SemverTag.init('v3.0.0+build.1')),                           # build
    ])
    def test_true(self, older_version: SemverTag, newer_version: SemverTag):
        self.assertTrue(older_version < newer_version)

    @parameterized.expand([
        (SemverTag.init('v1.0.0+build.1000'), SemverTag.init('v1.0.0+build.100')),
        (SemverTag.init('v1.0.0'), SemverTag.init('v1.0.0-alpha.1')),
        (SemverTag.init('v1.0.0'), SemverTag.init('v1.0.0-beta.1')),
        (SemverTag.init('v1.0.0'), SemverTag.init('v1.0.0-rc.1')),
        (SemverTag.init('1.0.5'), SemverTag.init('v1.0.0')),
        (SemverTag.init('v1.0.5'), SemverTag.init('1.0.0')),
        (SemverTag.init('v1.0.0-alpha.2'), SemverTag.init('v1.0.0-alpha.1')),
        (SemverTag.init('v1.0.0-beta.2'), SemverTag.init('v1.0.0-alpha.1')),
        (SemverTag.init('v1.0.0-rc.1'), SemverTag.init('v1.0.0-alpha.2')),
    ])
    def test_false(self, older_version: SemverTag, newer_version: SemverTag):
        self.assertFalse(older_version < newer_version)

    def setUp(self):
        super().setUp()
        self.repo_utils = PseudoRepo(self.config, self.repo)
