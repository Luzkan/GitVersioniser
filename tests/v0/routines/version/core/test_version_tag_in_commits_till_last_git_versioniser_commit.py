from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.version.routine import TestRoutineVersion


class TestVersionTagInCommitsTillLastGitversioniserCommit(TestRoutineVersion):
    @parameterized.expand([
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(1, 0, 1), [
            'A: Explicitly bumping patch. #patch',
        ]),
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(1, 1, 0), [
            'A: Explicitly bumping minor. #minor',
        ]),
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(2, 0, 0), [
            'A: Explicitly bumping major. #major',
        ]),
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(1, 0, 1, prerelease='alpha.1'), [
            'A: No Increment Tag.',
        ]),
    ])
    def test_basic_use(self, old_version, new_version, commit_messages):
        self.start_test(old_version, new_version, commit_messages)

    @parameterized.expand([
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(1, 0, 1, 'alpha.1'), [
            'A: Foo to Goo. #patch #alpha',
        ]),
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(1, 0, 1, 'beta.1'), [
            'A: Foo to Goo. #patch #beta',
        ]),
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(2, 0, 0, 'alpha.1'), [
            'A: Foo to Goo. #major #alpha',
        ]),
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(2, 0, 0, 'rc.1'), [
            'A: Foo to Goo. #major #prerelease',
        ]),
        (SemverTag.init_spec(1, 0, 0, 'alpha.1'), SemverTag.init_spec(1, 0, 0, 'alpha.2'), [
            'A: Foo to Goo. #alpha',
        ]),
        # TODO: The two below are not handled properly by external dependency.
        # (SemverTag.init_spec(1, 0, 0, 'alpha.1'), SemverTag.init_spec(1, 0, 0, 'beta.1'), [
        #     'A: Foo to Goo. #beta',
        # ]),
        # (SemverTag.init_spec(1, 0, 0, 'alpha.1'), SemverTag.init_spec(1, 0, 0, 'rc.1'), [
        #     'A: Foo to Goo. #prerelease',
        # ]),
        (SemverTag.init_spec(1, 0, 0, 'alpha.1'), SemverTag.init_spec(1, 0, 0, 'alpha.1', 'build.1'), [
            'A: Foo to Goo.',
        ]),
        (SemverTag.init_spec(2, 0, 0, 'rc.1'), SemverTag.init_spec(2, 0, 0), [
            'A: Foo to Goo. #fin',
        ]),
        (SemverTag.init_spec(2, 0, 0, 'beta.1', 'build.1'), SemverTag.init_spec(2, 0, 0), [
            'A: Foo to Goo. #fin',
        ]),
    ])
    def test_prereleases(self, old_version, new_version, commit_messages):
        self.start_test(old_version, new_version, commit_messages)

    @parameterized.expand([
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(1, 0, 1), [
            'F: Something. #patch #patch #patch',
        ]),
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(2, 0, 1), [
            'F: Something. #patch #patch #patch #major #patch #patch #patch',
        ]),
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(2, 1, 1), [
            'F: Something. #patch #patch #patch #major #minor #patch',
        ]),
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(2, 0, 0), [
            'F: Something. #major #fin #prerelease',
        ]),
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(2, 0, 0), [
            'F: Something. #major #prerelease #fin ',
        ]),
        (SemverTag.init_spec(1, 0, 0, 'rc.1', 'build.1'), SemverTag.init_spec(1, 0, 1, 'alpha.1'), [
            'F: Something. #fin',
            'F: Something. ',
        ]),
        (SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(2, 1, 3, 'alpha.1', 'build.1'), [
            'F: Something.',            # 1.0.1, 'alpha.1'
            'C: Something. #major',     # 2.0.0
            'R: Something. #minor',     # 2.1.0
            'S: Something. \n #patch',  # 2.1.1
            'R: Something. #patch',     # 2.1.2
            'A: Something.',            # 2.1.3, alpha.1
            'A: Something.',            # 2.1.3, alpha.1, 'build.1'
        ]),
        (SemverTag.init_spec(1, 0, 0, 'rc.4', build='build.1'), SemverTag.init_spec(2, 1, 3), [
            'F: Something.',
            'C: Something. #major',     # 2.0.0
            'R: Something. #minor',     # 2.1.0
            'S: Something. \n #patch',  # 2.1.1
            'R: Something. #patch',     # 2.1.2
            'A: Something.',            # 2.1.3, alpha.1
            'A: Something. #fin',       # 2.1.3
        ]),
    ])
    def test_advanced(self, old_version, new_version, commit_messages):
        self.start_test(old_version, new_version, commit_messages)

    def start_test(self, old_version, new_version, commit_messages):
        self.routine.repo.tags.create(str(old_version))
        self.repo_utils.create_gitversioniser_commit("A: This is last GitVerisoniser Commit.")
        self.repo_utils.create_commits(commit_messages)
        versions: Versions = self.routine.run()
        self.assertEqual(versions.new, new_version)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('VersionTagInCommitsTillLastGitVersioniserCommit')
        self.repo_utils = PseudoRepo(self.routine.config, self.routine.repo)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
