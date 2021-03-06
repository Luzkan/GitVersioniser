from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.changelog.routine import TestRoutineChangelog
from tests.v0.routines.changelog.utils.changelog import TestChangelogManager


class TestCommitChangeTags(TestRoutineChangelog):
    @parameterized.expand([
        (
            SemverTag.init_spec(1, 2, 3, 'rc.2', 'build.2'),
            [
                'Last GitVersioniser Commit',
                'A: Feature2',
                'A: Feature3',
                'F: Bugged Thing',
                'R: Useless Stuff',
            ],
            ('test_output_0',)
        ),
        (
            SemverTag.init_spec(1, 2, 3, 'rc.2', 'build.2'),
            [
                'Last GitVersioniser Commit',
                'C: Feature2',
                'C: Feature3',
                'R: Bugged Thing #minor \n #minor \n [1.2.3]',
                'R: Useless Stuff\nTest\nTest\nTest',
                'Sec: Useless Stuff',
                'Sec: Useless Stuff',
            ],
            ('test_output_1',)
        ),
        (
            SemverTag.init_spec(3, 63, 19, 'build.55323'),
            [
                'Last GitVersioniser Commit',
                'A: Added Add',
                'C: Changed Change',
                'Dep: Deprecated Deprecation ',
                'R: Removed Removal',
                'F: Fixed Fix',
                'Sec: Security Secure',
            ],
            ('test_output_2_1', 'test_output_2_2')
        ),
        (
            SemverTag.init('1.2.3-rc.1+build.1'),
            [
                'Last GitVersioniser Commit',
                'C: Feature1\n\n\n',
                'C: Feature2',
                'C: Feature3\n',
                'Change: Feature4',
                'C: Feature5\nHere is a small elaboration on the topic at hand.\nYeah.',
                'C: Feature6',
                'C: Feature7\nF: Fixed something here in the commit too!',
                'C: Feature8',
                'Sec: Security Feature 1',
                'Sec: Security Feature 2',
            ],
            ('test_output_3',)
        ),
        (
            SemverTag.init('1.2.3-rc.1+build.1'),
            [
                'Last GitVersioniser Commit',
                'Merge Commit #fin \n'
                '* C: Feature1\n\n'
                '* C: Feature2\n\n'
                '* C: Feature3\n\n'
                '* C: Feature4\n\n'
                '* C: Feature5\nHere is a small elaboration on the topic at hand.\nYeah.\n\n'
                '* C: Feature6\n\n'
                '* C: Feature7\nF: Fixed something here in the commit too!\n'
                '* C: Feature8\n\n'
                '* Sec: Security Feature 1\n\n'
                '* Sec: Security Feature 2\n',
            ],
            ('test_output_4',)
        ),
    ])
    def test_create_changelog(self, new_version: SemverTag, commit_messages: list[str], test_output_names: tuple[str]):
        def mini_routine(new_version: SemverTag, test_output: str):
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
        self.routine = self.get_routine('CommitChangeTags')
        self.repo_utils = PseudoRepo(self.routine.config, self.routine.repo)
        self.repo_utils.delete_remote()
        self.repo_utils.create_remote()
        self.test_changelog_manager = TestChangelogManager(self.routine, 'commit_change_tags')
        self.test_changelog_manager.rename_changelog_temporarily()

    def tearDown(self):
        self.repo_utils.delete_remote()
        self.test_changelog_manager.bring_back_old_changelog()
