from abc import ABC, abstractmethod
from dataclasses import dataclass

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.git_repository import GitRepository


@dataclass  # type: ignore [misc]
class Routine(ABC):
    config: Config
    repo: GitRepository

    def factory_name(self) -> str:
        def camel_to_snake_case(class_name: str):
            return ''.join(['_' + char.lower() if char.isupper() else char for char in class_name]).lstrip('_')
        return camel_to_snake_case(self.__class__.__name__)

    @abstractmethod
    def run(self, *args):
        pass
