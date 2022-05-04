from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from tests.v0.routines.commit_message.routine import TestRoutineCommitMessage


class TestSuffixVersionFullButOnlyDigits(TestRoutineCommitMessage):
    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('SuffixVersionFullButOnlyDigits')

    @parameterized.expand([
        (SemverTag.init_spec(1, 0, 0), 'Initial Commit', 'Initial Commit [`1.0.0`]'),
        (SemverTag.init_spec(2, 4, 6, 'rc.3', 'build.4'), 'F: Calculate Zombie Damage', 'F: Calculate Zombie Damage [`2.4.6-3+4`]'),
        (SemverTag.init_spec(0, 0, 0, build='build.1'), 'A: Heyy!', 'A: Heyy! [`0.0.0+1`]'),
        (SemverTag.init_spec(0, 0, 0, prerelease='rc.1'), ':3', ':3 [`0.0.0-1`]'),
        (SemverTag.init_spec(0, 0, 0, prerelease='rc.3', build='build.7'), ':3', ':3 [`0.0.0-3+7`]'),
    ])
    def test_true(self, version_info, commit_message, expected_commit_message):
        self.routine.repo.commits.commit(commit_message)
        self.assertEqual(self.routine.run(version_info).new, expected_commit_message)