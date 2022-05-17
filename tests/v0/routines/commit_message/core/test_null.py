from parameterized import parameterized

from gitversioniser.config.routines.commit_message import CommitMessageArguments
from gitversioniser.domain.repository.semver_tag import SemverTag
from tests.v0.routines.commit_message.routine import TestRoutineCommitMessage


class TestNull(TestRoutineCommitMessage):
    @parameterized.expand([
        (SemverTag.init_spec(4, 4, 4), '[`4.4.4`]'),
        (SemverTag.init_spec(1, 0, 999, build='build.4'), 'Patching Cyberpunk'),
        (SemverTag.init_spec(3, 2), 'R: Random personal file'),
        (SemverTag.init_spec(0, 0, 0, prerelease='rc.2'), 'I will never release')
    ])
    def test_null(self, version_info: SemverTag, commit_message: str):
        routine = self.get_routine(CommitMessageArguments('Null', 'FullButOnlyDigits', 'Null', 'Null'))
        routine.repo.commits.commit(commit_message)
        self.assertEqual(str(routine.run(version_info).new), commit_message)
