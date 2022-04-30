from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.helpers.versions import Versions
from tests.v0.routines.version.routine import TestRoutineVersion


class TestCommitsTillLastGitversioniserCommit(TestRoutineVersion):
    def create_commits(self, commit_messages):
        git_versioniser_author_argument = f"--author={self.routine.config.credentials.username} <{self.routine.config.credentials.email}>"
        self.routine.target_repo.repo.git.commit("--allow-empty", "-m", commit_messages[0], git_versioniser_author_argument)
        for commit_message in commit_messages[1:]:
            self.routine.target_repo.repo.git.commit("--allow-empty", "-m", commit_message, "--author=Bob <bob@github.com>")

    @parameterized.expand([
        (VersionInfo(1, 2, 3), VersionInfo(2, 1, 2, build='build.1'), [
            'A: New Feature #patch',  # This one is made by supposedly gitversioniser
            'F: New Feature',
            'C: New Feature #major',
            'R: New Feature #minor',
            'S: New Feature \n #patch',
            'R: New Feature #patch',
            'A: New Feature',
        ]),
        (VersionInfo(1, 88, 232, 'rc.4', build='build.1'), VersionInfo(2, 1, 2, build='build.1'), [
            'A: New Feature',  # This one is made by supposedly gitversioniser
            'F: New Feature',
            'C: New Feature #major',
            'R: New Feature #minor',
            'S: New Feature \n #patch',
            'R: New Feature #patch',
            'A: New Feature',
        ]),
    ])
    def test_true(self, old_version, new_version, commit_messages):
        self.routine.target_repo.tags.create(str(old_version))
        self.create_commits(commit_messages)
        versions: Versions = self.routine.run()
        self.assertEqual(versions.new, new_version)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('commits_till_last_gitversioniser_commit')

    def tearDown(self):
        for tag in self.routine.target_repo.tags.get_sorted:
            self.routine.target_repo.repo.git.tag('-d', tag)
