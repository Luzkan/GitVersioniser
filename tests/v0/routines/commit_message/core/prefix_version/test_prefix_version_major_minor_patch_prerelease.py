from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from tests.v0.routines.commit_message.routine import TestRoutineCommitMessage


class TestPrefixVersionMajorMinorPatchPrerelease(TestRoutineCommitMessage):
    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('prefix_version_major_minor_patch_prerelease')

    @parameterized.expand([
        (SemverTag.init_spec(1, 0, 0), 'Initial Commit', '[`1.0.0`] Initial Commit'),
        (SemverTag.init_spec(2, 4, 6, 'rc.3', 'build.4'), 'F: Calculate Zombie Damage', '[`2.4.6-rc.3`] F: Calculate Zombie Damage'),
        (SemverTag.init_spec(0, 0, 0, build='build.1'), 'A: Heyy!', '[`0.0.0`] A: Heyy!'),
        (SemverTag.init_spec(0, 0, 0, prerelease='rc.1'), ':3', '[`0.0.0-rc.1`] :3'),
        (SemverTag.init_spec(0, 0, 0, prerelease='rc.3', build='build.7'), ':3', '[`0.0.0-rc.3`] :3'),
    ])
    def test_true(self, version_info, commit_message, expected_commit_message):
        self.routine.repo.commits.commit(commit_message)
        self.assertEqual(self.routine.run(version_info).new, expected_commit_message)
