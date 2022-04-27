from parameterized import parameterized
from semver import VersionInfo

from tests.v0.routines.commit_message.routine import TestRoutineCommitMessage


class TestPrefixTag(TestRoutineCommitMessage):
    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('prefix_tag')

    @parameterized.expand([
        (VersionInfo(1, 0, 0), 'Initial Commit', '[`1.0.0`] Initial Commit'),
        (VersionInfo(2, 4, 6, 'alpha', 'build.4'), 'F: Calculate Zombie Damage', '[`2.4.6-alpha+build.4`] F: Calculate Zombie Damage'),
        (VersionInfo(0, 0, 0, build='build.1'), 'A: Heyy!', '[`0.0.0+build.1`] A: Heyy!'),
        (VersionInfo(0, 0, 0, prerelease='beta'), ':3', '[`0.0.0-beta`] :3')
    ])
    def test_prefix(self, version_info, commit_message, expected_commit_message):
        self.routine.target_repo.commits.commit(commit_message)
        self.assertEqual(self.routine.run(version_info), expected_commit_message)

    # TODO: Sanitize commit inputs first.
    # from hypothesis import given
    # from hypothesis.strategies import text
    # @given(text(min_size=1))
    # def test_prefix_exhausted(self, text):
    #     self.routine = self.get_routine('prefix_tag')
    #     self.routine.target_repo.commits.commit(text)
    #     self.assertEqual(self.routine.run(VersionInfo(0, 1, 0)), f"[`0.1.0`] {text}")
