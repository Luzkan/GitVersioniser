from abc import ABC, abstractmethod
from dataclasses import dataclass

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.git_repository import GitRepository


@dataclass  # type: ignore [misc]
class Routine(ABC):
    config: Config
    repo: GitRepository

    def factory_name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def run(self, *args):
        pass
