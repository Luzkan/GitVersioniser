from abc import ABC, abstractmethod
from dataclasses import dataclass

from config.config import Config
from domain.repository.git_repository import GitRepository


@dataclass
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
