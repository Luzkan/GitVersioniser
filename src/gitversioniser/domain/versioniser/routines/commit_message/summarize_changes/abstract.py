from abc import ABC, abstractmethod

from gitversioniser.config.patterns.commit_change_tags.abstract import CommitMessageLine
from gitversioniser.domain.versioniser.routines.abstract import Routine


class SummarizeChanges(Routine, ABC):

    @staticmethod
    @abstractmethod
    def run(list_of_changes: list[CommitMessageLine], summary: str) -> str:
        pass
