from abc import ABC, abstractmethod

from gitversioniser.config.patterns.commit_change_tags.abstract import CommitMessageLine
from gitversioniser.domain.versioniser.routines.abstract import Routine


class DescribeChanges(Routine, ABC):

    @staticmethod
    @abstractmethod
    def run(list_of_changes: list[CommitMessageLine], description: str) -> str:
        pass
