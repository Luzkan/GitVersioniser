from unittest.mock import Mock

from git import GitCommandError
from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.helpers.versions import Versions
from tests.v0.routines.commiting.routine import TestRoutineCommiting


class TestPushMainNew(TestRoutineCommiting):
    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('push_main_new')

    def cant_test_through_routine_because_no_remote_assigned(self, commit_message_for_amend: str):
        try:
            self.routine.run(VersioningResult(Versions(VersionInfo(1, 0, 0), VersionInfo(1, 0, 0)), commit_message_for_amend, Mock, Mock))
        except GitCommandError as error:
            self.assertEqual(error.args[0], ['git', 'pull', '--ff-only'])

    @parameterized.expand([
        ('Initial Commit', '[`1.0.0`] Initial Commit'),
        ('Tbh, this just', 'tests that, the'),
        ('git commit works', 'through the git library')
    ])
    def test_push_main_new(self, last_commit_message, new_commit_message):
        self.routine.target_repo.commits.commit(last_commit_message)
        self.cant_test_through_routine_because_no_remote_assigned(new_commit_message)
        self.routine.target_repo.files.add_all()
        self.routine.target_repo.commits.commit(new_commit_message)
        self.assertEqual(self.routine.target_repo.commits.latest.message.value, f"{new_commit_message}\n")
        self.assertEqual(self.routine.target_repo.commits.latest.get_parent().message.value, f"{last_commit_message}\n")
