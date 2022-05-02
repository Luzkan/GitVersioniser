from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.changelog.routine import TestRoutineChangelog
from tests.v0.routines.changelog.utils.changelog import TestChangelogManager


class TestLastCommitAsSummary(TestRoutineChangelog):
    @parameterized.expand([
        (
            SemverTag.init_spec(1, 2, 3, 'rc.2', 'build.2'),
            [
                'R: Something',
                'C: Something1',
                'C: Something2',
                'F: Bugged Thing',
                'Feature: New Mechanism\nThis is a description of the Merge Request\nMaybe a little bit more messages',
            ],
            ('test_output_1',)
        ),
        (
            SemverTag.init_spec(1, 2, 3, 'rc.2', 'build.2'),
            [
                'R: Something',
                'A: Feature\nSome Text\nMaybe a little bit more messages',
            ],
            ('test_output_2',)
        ),
        (
            SemverTag.init_spec(3, 63, 19, 'build.55323'),
            [
                'R: Something',
                '### Styling markdown\n\n#### Right from the commit message\n\n- Test1\n- Test2\n- Test3',
            ],
            ('test_output_3_1', 'test_output_3_2')
        ),
    ])
    def test_create_changelog(self, new_version: SemverTag, commit_messages: list[str], test_output_names: tuple[str]):
        def mini_routine(new_version: SemverTag, test_output: str) -> None:
            self.repo_utils.create_gitversioniser_commit(commit_messages[0])
            self.repo_utils.create_commits(commit_messages[1:])
            self.routine.run(new_version)
            self.assertEqual(
                self.test_changelog_manager.get_changelog_generated_content(),
                self.test_changelog_manager.get_changelog_test_content(test_output)
            )

        for test_output_name in test_output_names:
            new_version = new_version.bump_build()
            mini_routine(new_version, test_output_name)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('last_commit_message_as_description')
        self.repo_utils = PseudoRepo(self.routine.config, self.routine.repo)
        self.repo_utils.delete_remote()
        self.repo_utils.create_remote()
        self.test_changelog_manager = TestChangelogManager(self.routine, 'last_commit_message_as_description')
        self.test_changelog_manager.rename_changelog_temporarily()

    def tearDown(self):
        self.repo_utils.delete_remote()
        self.test_changelog_manager.bring_back_old_changelog()
