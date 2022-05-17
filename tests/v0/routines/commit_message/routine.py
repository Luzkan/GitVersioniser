from git.repo import Repo

from gitversioniser.config.routines.commit_message import CommitMessageArguments
from gitversioniser.domain.repository.git_repository import GitRepository
from gitversioniser.domain.versioniser.routines.commit_message.factory import RoutineCommitMessageFactory
from tests.utils.temp_directory import TempDirectory
from tests.v0.default_scenario_v0 import TestDefaultScenarioV0


class TestRoutineCommitMessage(TestDefaultScenarioV0):
    def get_routine(self, commit_message_arguments: CommitMessageArguments):
        deps = (self.config, GitRepository(self.config, _repo=Repo.init(self.test_repo_path)))
        return RoutineCommitMessageFactory(commit_message_arguments).create(deps)

    def setUp(self):
        super().setUp()
        self.temp_directory = TempDirectory(self.test_repo_path)
