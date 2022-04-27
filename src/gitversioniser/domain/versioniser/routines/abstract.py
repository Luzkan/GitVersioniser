from abc import ABC, abstractmethod
from dataclasses import dataclass

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.git_repository import GitRepository


@dataclass  # type: ignore [misc]
class Routine(ABC):
    config: Config
    target_repo: GitRepository

    @staticmethod
    @abstractmethod
    def factory_name() -> str:
        pass

    @abstractmethod
    def run(self):
        pass
