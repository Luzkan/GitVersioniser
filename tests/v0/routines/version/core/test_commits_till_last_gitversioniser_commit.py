from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.version.routine import TestRoutineVersion


class TestCommitsTillLastGitversioniserCommit(TestRoutineVersion):
    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(2, 1, 2, build='build.1'), [
            'A: New Feature #patch',
            'F: New Feature',
            'C: New Feature #major',
            'R: New Feature #minor',
            'S: New Feature \n #patch',
            'R: New Feature #patch',
            'A: New Feature',
        ]),
        (VersionInfo(1, 88, 232, 'rc.4', build='build.1'), VersionInfo(2, 1, 2, build='build.1'), [
            'A: New Feature',
            'F: New Feature',
            'C: New Feature #major',
            'R: New Feature #minor',
            'S: New Feature \n #patch',
            'R: New Feature #patch',
            'A: New Feature',
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
        self.routine = self.get_routine('commits_till_last_gitversioniser_commit')
        self.repo_utils = PseudoRepo(self.routine)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
