from git.repo import Repo

from gitversioniser.domain.repository.git_repository import GitRepository
from gitversioniser.domain.versioniser.routines.tagging.factory import RoutineTaggingFactory
from gitversioniser.helpers.types import ROUTINE_TAGGING_TYPE
from tests.utils.temp_directory import TempDirectory
from tests.v0.utils.default_v0 import TestDefaultV0


class TestRoutineTagging(TestDefaultV0):
    def get_routine(self, routine_name: ROUTINE_TAGGING_TYPE):
        return RoutineTaggingFactory.create(routine_name)(self.config, GitRepository(self.config, _repo=Repo.init(self.test_repo_path, mkdir=True)))

    def setUp(self):
        super().setUp()
        self.temp_directory = TempDirectory(self.test_repo_path)
