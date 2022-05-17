from abc import ABC, abstractmethod

from gitversioniser.domain.versioniser.routines.abstract import Routine


class PlaceVersionTag(Routine, ABC):

    @staticmethod
    @abstractmethod
    def run(new_version: str, message: str) -> str:
        pass
