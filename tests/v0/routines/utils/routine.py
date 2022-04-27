from git.repo import Repo

from gitversioniser.domain.repository.git_repository import GitRepository
from gitversioniser.domain.versioniser.routines.commit_message.factory import RoutineCommitFactory
from gitversioniser.helpers.types import ROUTINE_COMMIT_MESSAGE_TYPE
from tests.v0.utils.default_v0 import TestDefaultV0


class TestRoutine(TestDefaultV0):
    def get_routine(self, routine_name: ROUTINE_COMMIT_MESSAGE_TYPE):
        return RoutineCommitFactory.create(routine_name)(self.config, GitRepository(self.config, repo=Repo.init(self.test_repo_path)))

    def setUp(self):
        super().setUp()
