from git.repo import Repo

from gitversioniser.domain.repository.git_repository import GitRepository
from gitversioniser.domain.versioniser.routines.commiting.factory import RoutineCommitingFactory
from gitversioniser.helpers.types import ROUTINE_COMMITING_TYPE
from tests.utils.temp_directory import TempDirectory
from tests.v0.default_scenario_v0 import TestDefaultScenarioV0


class TestRoutineCommiting(TestDefaultScenarioV0):
    def get_routine(self, routine_name: ROUTINE_COMMITING_TYPE):
        return RoutineCommitingFactory.create(routine_name)(self.config, GitRepository(self.config, _repo=Repo.init(self.test_repo_path, mkdir=True)))

    def setUp(self):
        super().setUp()
        self.temp_directory = TempDirectory(self.test_repo_path)
