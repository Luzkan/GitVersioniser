from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from tests.v0.routines.commit_message.routine import TestRoutineCommitMessage


class TestSuffixTag(TestRoutineCommitMessage):
    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('suffix_version_full')

    @parameterized.expand([
        (SemverTag.init_spec(4, 4, 4), '[`4.4.4`]', '[`4.4.4`] [`4.4.4`]'),
        (SemverTag.init_spec(1, 0, 999, build='build.4'), 'Patching Cyberpunk', 'Patching Cyberpunk [`1.0.999+build.4`]'),
        (SemverTag.init_spec(3, 2), 'R: Random personal file', 'R: Random personal file [`3.2.0`]'),
        (SemverTag.init_spec(0, 0, 0, prerelease='gamma'), 'I will never release', 'I will never release [`0.0.0-gamma`]')
    ])
    def test_suffix(self, version_info, commit_message, expected_commit_message):
        self.routine.repo.commits.commit(commit_message)
        self.assertEqual(self.routine.run(version_info).new, expected_commit_message)
