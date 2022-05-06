from dataclasses import dataclass

from git.repo import Repo

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.git_repository import GitRepository
from gitversioniser.domain.versioniser.routines.manager import RoutineManager


@dataclass
class Versioniser:
    config: Config

    def __post_init__(self):
        self.repository = GitRepository(self.config, _repo=Repo(self.config.target_repository_path))
        self.routine_manager = RoutineManager(self.config, self.repository)

    def run(self) -> None:
        self.routine_manager.run()
