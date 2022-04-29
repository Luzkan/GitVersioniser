from parameterized import parameterized
from semver import VersionInfo

from tests.v0.routines.commit_message.routine import TestRoutineCommitMessage


class TestSuffixTag(TestRoutineCommitMessage):
    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('suffix_version')

    @parameterized.expand([
        (VersionInfo(4, 4, 4), '[`4.4.4`]', '[`4.4.4`] [`4.4.4`]'),
        (VersionInfo(1, 0, 999, build='build.4'), 'Patching Cyberpunk', 'Patching Cyberpunk [`1.0.999+build.4`]'),
        (VersionInfo(3, 2), 'R: Random personal file', 'R: Random personal file [`3.2.0`]'),
        (VersionInfo(0, 0, 0, prerelease='gamma'), 'I will never release', 'I will never release [`0.0.0-gamma`]')
    ])
    def test_suffix(self, version_info, commit_message, expected_commit_message):
        self.routine.target_repo.commits.commit(commit_message)
        self.assertEqual(self.routine.run(version_info), expected_commit_message)

    # TODO: Sanitize commit inputs first.
    # @given(text(min_size=1))
    # def test_suffix_exhausted(self, text):
    #     self.routine = self.get_routine('prefix_tag')
    #     self.routine.target_repo.commits.commit(text)
    #     self.assertEqual(self.routine.run(VersionInfo(0, 0, 1)), f"{text} [`0.0.1`]")
