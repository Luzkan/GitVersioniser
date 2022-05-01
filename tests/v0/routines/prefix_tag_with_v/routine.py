from git.repo import Repo

from gitversioniser.domain.repository.git_repository import GitRepository
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.factory import RoutinePrefixTagWithVFactory
from gitversioniser.helpers.types import ROUTINE_PREFIX_TAG_WITH_V
from tests.utils.temp_directory import TempDirectory
from tests.v0.default_scenario_v0 import TestDefaultScenarioV0


class TestRoutinePrefixTagWithV(TestDefaultScenarioV0):
    def get_routine(self, routine_name: ROUTINE_PREFIX_TAG_WITH_V):
        return RoutinePrefixTagWithVFactory.create(routine_name)(
            self.config, GitRepository(self.config, _repo=Repo.init(self.test_repo_path, mkdir=True))
        )

    def setUp(self):
        super().setUp()
        self.temp_directory = TempDirectory(self.test_repo_path)
