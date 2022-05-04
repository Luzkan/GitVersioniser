from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.version.routine import TestRoutineVersion


class TestCommitsTillLastGitversioniserCommit(TestRoutineVersion):
    @parameterized.expand([
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 3, 0), [
            'A: This is last GitVerisoniser Commit.',
            'F: Something. #minor',
        ]),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 3, 0, prerelease='alpha.1'), [
            'A: This is last GitVerisoniser Commit.',
            'F: Something. #minor #alpha',
        ]),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 3, 0, prerelease='alpha.1'), [
            'A: This is last GitVerisoniser Commit.',
            'F: Something. #alpha #minor',
        ]),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(1, 2, 4), [
            'A: This is last GitVerisoniser Commit.',
            'F: Something. #patch #patch #patch',
        ]),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(2, 1, 1), [
            'A: This is last GitVerisoniser Commit.',
            'F: Something. #patch #major #minor #patch',
        ]),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(2, 0, 0, prerelease='beta.1'), [
            'A: This is last GitVerisoniser Commit.',
            'F: Something. #major #beta',
        ]),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(2, 0, 0, prerelease='rc.1'), [
            'A: This is last GitVerisoniser Commit.',
            'F: Something. #major #prerelease',
        ]),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(2, 0, 0), [
            'A: This is last GitVerisoniser Commit.',
            'F: Something. #major #fin #prerelease',
        ]),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(2, 0, 0), [
            'A: This is last GitVerisoniser Commit.',
            'F: Something. #major #prerelease #fin ',
        ]),
        (SemverTag.init_spec(1, 88, 232, 'rc.4', build='build.1'), SemverTag.init_spec(1, 88, 232, build='build.1'), [
            'A: This is last GitVerisoniser Commit.',
            'F: Something. #fin',
            'F: Something. ',
        ]),
        (SemverTag.init_spec(1, 2, 3), SemverTag.init_spec(2, 1, 2, build='build.1'), [
            'A: This is last GitVerisoniser Commit. #patch',
            'F: Something.',
            'C: Something. #major',
            'R: Something. #minor',
            'S: Something. \n #patch',
            'R: Something. #patch',
            'A: Something.',
        ]),
        (SemverTag.init_spec(1, 88, 232, 'rc.4', build='build.1'), SemverTag.init_spec(2, 1, 2, build='build.1'), [
            'A: This is last GitVerisoniser Commit.',
            'F: Something.',
            'C: Something. #major',
            'R: Something. #minor',
            'S: Something. \n #patch',
            'R: Something. #patch',
            'A: Something.',
        ]),
    ])
    def test_true(self, old_version, new_version, commit_messages):
        self.routine.repo.tags.create(str(old_version))
        self.repo_utils.create_gitversioniser_commit(commit_messages[0])
        self.repo_utils.create_commits(commit_messages[1:])
        versions: Versions = self.routine.run()
        self.assertEqual(versions.new, new_version)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('commits_till_last_git_versioniser_commit')
        self.repo_utils = PseudoRepo(self.routine.config, self.routine.repo)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
