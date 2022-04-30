from dataclasses import dataclass, field

from git.repo import Repo

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.git_repository import GitRepository
from gitversioniser.domain.versioniser.routines.manager import RoutineManager


@dataclass
class Versioniser:
    config: Config
    target_repo: GitRepository = field(init=False)
    routine_manager: RoutineManager = field(init=False)

    def __post_init__(self):
        def init_dependencies():
            self.target_repo = GitRepository(self.config, repo=Repo(self.config.target_repository_path))

        def init_submodules():
            self.routine_manager = RoutineManager(self.config, self.target_repo)

        init_dependencies()
        init_submodules()

    def run(self) -> None:
        self.routine_manager.run()
