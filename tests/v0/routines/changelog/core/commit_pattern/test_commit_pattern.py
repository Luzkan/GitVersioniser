from parameterized import parameterized
from semver import VersionInfo

from tests.utils.repo_utils import RepoUtils
from tests.v0.routines.changelog.routine import TestRoutineChangelog
from tests.v0.routines.changelog.utils.changelog import TestChangelogManager


class TestCommitPattern(TestRoutineChangelog):
    @parameterized.expand([
        (
            VersionInfo(1, 2, 3, 'rc.2', 'build.2'),
            [
                'A: Feature1',
                'A: Feature2',
                'A: Feature3',
                'F: Bugged Thing',
                'R: Useless Stuff',
            ],
            ('test_output_1',)
        ),
        (
            VersionInfo(1, 2, 3, 'rc.2', 'build.2'),
            [
                'C: Feature1',
                'C: Feature2',
                'C: Feature3',
                'R: Bugged Thing #minor \n #minor \n [1.2.3]',
                'R: Useless Stuff\nTest\nTest\nTest',
                'S: Useless Stuff',
                'S: Useless Stuff',
            ],
            ('test_output_2',)
        ),
        (
            VersionInfo(3, 63, 19, 'build.55323'),
            [
                'A: Versioniser',
                'A: Added Add',
                'C: Changed Change',
                'D: Deprecated Deprecation ',
                'R: Removed Removal',
                'F: Fixed Fix',
                'S: Security Secure',
            ],
            ('test_output_3_1', 'test_output_3_2')
        ),
    ])
    def test_create_changelog(self, new_version: VersionInfo, commit_messages: list[str], test_output_names: tuple[str]):
        def mini_routine(new_version: VersionInfo, test_output: str):
            self.repo_utils.create_gitversioniser_commit(commit_messages[0])
            self.repo_utils.create_commits(commit_messages[1:])
            self.routine.run(new_version)
            self.assertEqual(
                self.test_changelog_manager.get_changelog_generated_content(),
                self.test_changelog_manager.get_changelog_test_content(test_output)
            )

        for test_output_name in test_output_names:
            mini_routine(new_version.bump_build(), test_output_name)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('commit_pattern')
        self.repo_utils = RepoUtils(self.routine)
        self.repo_utils.delete_remote()
        self.repo_utils.create_remote()
        self.test_changelog_manager = TestChangelogManager(self.routine, 'commit_pattern')
        self.test_changelog_manager.rename_changelog_temporarily()

    def tearDown(self):
        self.repo_utils.delete_remote()
        self.test_changelog_manager.bring_back_old_changelog()
