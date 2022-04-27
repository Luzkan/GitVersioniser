from abc import ABC, abstractmethod

from semver import VersionInfo

from gitversioniser.domain.versioniser.routines.abstract import Routine


class RoutineCommitMessage(Routine, ABC):
    @abstractmethod
    def run(self, new_version: VersionInfo) -> str:
        pass
