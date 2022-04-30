from parameterized import parameterized
from semver import VersionInfo

from tests.v0.routines.changelog.routine import TestRoutineChangelog
from tests.v0.routines.changelog.utils.changelog import TestChangelogManager


class TestLastCommitAsSummary(TestRoutineChangelog):
    def create_commits(self, commit_messages):
        git_versioniser_author_argument = f"--author={self.routine.config.credentials.username} <{self.routine.config.credentials.email}>"
        self.routine.target_repo.repo.git.commit("--allow-empty", "-m", commit_messages[0], git_versioniser_author_argument)
        for commit_message in commit_messages[1:]:
            self.routine.target_repo.repo.git.commit("--allow-empty", "-m", commit_message, "--author=Bob <bob@github.com>")

    @parameterized.expand([
        (VersionInfo(1, 2, 3, 'rc.2', 'build.2'), [
            'R: Something',
            'C: Something1',
            'C: Something2',
            'F: Bugged Thing',
            'Feature: New Mechanism\nThis is a description of the Merge Request\nMaybe a little bit more messages',
        ]),
    ])
    def test_create_changelog_1(self, new_version, commit_messages):
        self.create_commits(commit_messages)
        self.routine.run(new_version)
        generated = self.test_changelog_manager.get_changelog_generated_content()
        output = self.test_changelog_manager.get_changelog_test_content('test_output_1')
        self.assertEqual(generated, output)

    @parameterized.expand([
        (VersionInfo(1, 2, 3, 'rc.2', 'build.2'), [
            'R: Something',
            'A: Feature\nSome Text\nMaybe a little bit more messages',
        ]),
    ])
    def test_create_changelog_2(self, new_version, commit_messages):
        self.create_commits(commit_messages)
        self.routine.run(new_version)
        generated = self.test_changelog_manager.get_changelog_generated_content()
        output = self.test_changelog_manager.get_changelog_test_content('test_output_2')
        self.assertEqual(generated, output)

    @parameterized.expand([
        (VersionInfo(3, 63, 19, 'build.55323'), [
            'R: Something',
            '### Styling markdown\n\n#### Right from the commit message\n\n- Test1\n- Test2\n- Test3',
        ]),
    ])
    def test_create_changelog_3(self, new_version: VersionInfo, commit_messages):
        def mini_routine(new_version: VersionInfo, test_output: str):
            self.create_commits(commit_messages)
            self.routine.run(new_version)
            generated = self.test_changelog_manager.get_changelog_generated_content()
            output = self.test_changelog_manager.get_changelog_test_content(test_output)
            self.assertEqual(generated, output)

        mini_routine(new_version, 'test_output_3_1')
        mini_routine(new_version.bump_build(), 'test_output_3_2')

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('last_commit_message_as_description')
        self.test_changelog_manager = TestChangelogManager(self.routine, 'last_commit_message_as_description')
        self.test_changelog_manager.delete_remotes()
        self.test_changelog_manager.create_remotes()
        self.test_changelog_manager.rename_changelog_temporarily()

    def tearDown(self):
        self.test_changelog_manager.delete_remotes()
        self.test_changelog_manager.bring_back_old_changelog()
