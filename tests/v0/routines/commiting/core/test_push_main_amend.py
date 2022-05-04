from unittest.mock import Mock

from git import GitCommandError
from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.commit_message.utils.commit_message_result import CommitMessageResult
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult
from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.v0.routines.commiting.routine import TestRoutineCommiting


class TestPushMainAmend(TestRoutineCommiting):
    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('push_origin_amend')

    def cant_test_through_routine_because_no_remote_assigned(self, commit_message_for_amend: str):
        try:
            self.routine.run(VersioningResult(
                Versions(SemverTag.init_spec(1, 0, 0), SemverTag.init_spec(1, 0, 0)),
                CommitMessageResult(old=Mock, new=commit_message_for_amend),
                Mock, Mock, Mock
            ))
        except GitCommandError as error:
            self.assertEqual(error.args[0], ['git', 'pull', '--ff-only'])

    @parameterized.expand([
        ('Initial Commit', '[`1.0.0`] Initial Commit'),
        ('Tbh, this just', 'tests that, the'),
        ('git amend works', 'through the git library')
    ])
    def test_commit_amend(self, commit_message, commit_message_for_amend):
        self.routine.repo.commits.commit(commit_message)
        self.cant_test_through_routine_because_no_remote_assigned(commit_message_for_amend)
        self.routine.repo.files.add_all()
        self.routine.repo.commits.commit_amend(commit_message_for_amend)
        self.assertEqual(self.routine.repo.commits.latest.message.value, f"{commit_message_for_amend}\n")
