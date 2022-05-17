from abc import ABC, abstractmethod

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.abstract import Routine


class FormatVersionTag(Routine, ABC):
    @staticmethod
    @abstractmethod
    def run(new_version: SemverTag) -> str:
        pass
