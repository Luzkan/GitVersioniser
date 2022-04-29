from parameterized import parameterized
from semver import VersionInfo

from tests.v0.routines.commit_message.routine import TestRoutineCommitMessage


class TestNull(TestRoutineCommitMessage):
    @parameterized.expand([
        (VersionInfo(4, 4, 4), '[`4.4.4`]'),
        (VersionInfo(1, 0, 999, build='build.4'), 'Patching Cyberpunk'),
        (VersionInfo(3, 2), 'R: Random personal file'),
        (VersionInfo(0, 0, 0, prerelease='rc.2'), 'I will never release')
    ])
    def test_null(self, version_info, commit_message,):
        self.routine = self.get_routine('null')
        self.routine.target_repo.commits.commit(commit_message)
        self.assertEqual(self.routine.run(version_info), commit_message)
