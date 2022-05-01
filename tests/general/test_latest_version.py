from parameterized import parameterized
from semver import VersionInfo

from tests.general.general_scenario import TestGeneralScenario
from tests.utils.pseudo_repo import PseudoRepo


class TestLatestVersion(TestGeneralScenario):
    @parameterized.expand([
        (VersionInfo(1, 2, 5), [VersionInfo(1, 2, 3), VersionInfo(1, 2, 4), VersionInfo(1, 2, 5)], ),
        (VersionInfo(1, 2, 3, prerelease='alpha.3'), [
            VersionInfo(1, 2, 3, prerelease='alpha.1'),
            VersionInfo(1, 2, 3, prerelease='alpha.2'),
            VersionInfo(1, 2, 3, prerelease='alpha.3')
        ]),
        (VersionInfo(1, 2, 3, prerelease='rc.1'), [
            VersionInfo(1, 2, 3, prerelease='alpha.1'),
            VersionInfo(1, 2, 3, prerelease='beta.1'),
            VersionInfo(1, 2, 3, prerelease='rc.1')
        ]),
        (VersionInfo(1, 2, 3, prerelease='rc.1'), [
            VersionInfo(1, 2, 3, prerelease='rc.1'),
            VersionInfo(1, 2, 3, prerelease='alpha.1'),
            VersionInfo(1, 2, 3, prerelease='beta.1')
        ]),
        (VersionInfo(1, 2, 3, prerelease='rc.1'), [
            VersionInfo(1, 2, 3, prerelease='rc.1'),
            VersionInfo(1, 2, 3, prerelease='alpha.3'),
            VersionInfo(1, 2, 3, prerelease='beta.5')
        ]),
    ])
    def test_latest_semver(self, should_be_latest: VersionInfo, versions: list[VersionInfo], ):
        for version in versions:
            self.repo.tags.create(str(version))
        self.assertEqual(self.repo.tags.latest_semver, should_be_latest)

    @parameterized.expand([
        (VersionInfo(1, 2, 3), ['abc', 'def', '1.2.3'], ),
        (VersionInfo(1, 2, 4), [
            '1.2.3+build.1',
            'v1.2.4',
            '1.2.3-rc.1+build.3'
        ]),
        (VersionInfo(1, 2, 6), [
            'v1.2.5+build.1',
            'v1.2.4',
            '1.2.6',
            '1.2.3-rc.1+build.3'
        ]),
        (VersionInfo(1, 2, 6), [
            '1.2.5+build.1',
            '1.2.4',
            'v1.2.6',
            'v1.2.3-rc.1+build.3'
        ]),
        (VersionInfo(1, 2, 6), [
            '1.2.5+build.1',
            'Test_1.2.8',
            '1.2.8_Test',
            'vv1.2.8',
            'v1.2.6',
            'v1.2.3-rc.1+build.3'
        ]),
    ])
    def test_latest_semver_via_string(self, should_be_latest: VersionInfo, versions: list[str], ):
        for version in versions:
            self.repo.tags.create(str(version))
        self.assertEqual(self.repo.tags.latest_semver, should_be_latest)

    def setUp(self):
        super().setUp()
        self.repo_utils = PseudoRepo(self.config, self.repo)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
