from parameterized import parameterized
from semver import VersionInfo

from tests.v0.routines.commit_message.routine import TestRoutineCommitMessage


class TestPrefixVersionMajorMinorPatch(TestRoutineCommitMessage):
    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('suffix_version_major_minor_patch')

    @parameterized.expand([
        (VersionInfo(1, 0, 0), 'Initial Commit', 'Initial Commit [`1.0.0`]'),
        (VersionInfo(2, 4, 6, 'rc.3', 'build.4'), 'F: Calculate Zombie Damage', 'F: Calculate Zombie Damage [`2.4.6`]'),
        (VersionInfo(0, 0, 0, build='build.1'), 'A: Heyy!', 'A: Heyy! [`0.0.0`]'),
        (VersionInfo(0, 0, 0, prerelease='rc.1'), ':3', ':3 [`0.0.0`]'),
        (VersionInfo(0, 0, 0, prerelease='rc.3', build='build.7'), ':3', ':3 [`0.0.0`]'),
    ])
    def test_true(self, version_info, commit_message, expected_commit_message):
        self.routine.target_repo.commits.commit(commit_message)
        self.assertEqual(self.routine.run(version_info), expected_commit_message)