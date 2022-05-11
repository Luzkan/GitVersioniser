from abc import ABC
from dataclasses import dataclass

from gitversioniser.config.patterns.commit_increment_tags.increment import Increment


@dataclass(frozen=True)
class CommitIncrementTags(ABC):
    def parse_increments(self, commit_message: str) -> list[Increment]:
        return [increment for increment in self.__dict__.values() if str(increment.pattern) in commit_message]

    def has_increment(self, commit_message: str) -> bool:
        return any([increment.pattern in commit_message for increment in self.__dict__.values()])
