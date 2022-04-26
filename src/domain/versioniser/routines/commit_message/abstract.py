from abc import ABC, abstractmethod
from dataclasses import dataclass

from semver import VersionInfo

from domain.versioniser.routines.abstract import Routine


@dataclass
class RoutineCommitMessage(Routine, ABC):
    @abstractmethod
    def run(self, new_version: VersionInfo) -> str:
        pass
