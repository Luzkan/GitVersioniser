from unittest.mock import Mock

from git import GitCommandError
from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult
from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.v0.routines.commiting.routine import TestRoutineCommiting


class TestPushMainAmend(TestRoutineCommiting):
    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('push_main_amend')

    def cant_test_through_routine_because_no_remote_assigned(self, commit_message_for_amend):
        try:
            self.routine.run(VersioningResult(Versions(VersionInfo(1, 0, 0), VersionInfo(1, 0, 0)), commit_message_for_amend, Mock, Mock, Mock))
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
