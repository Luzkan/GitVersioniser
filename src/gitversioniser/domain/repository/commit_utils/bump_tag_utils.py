from dataclasses import dataclass

from gitversioniser.config.commit_increment_tags.increment import Increment
from gitversioniser.domain.repository.commit_utils.tag import TagUtils


@dataclass
class IncrementTagUtils(TagUtils):
    def exist(self) -> bool:
        return self.config.patterns.increments.has_increment(self.value.lower())

    def get(self) -> list[Increment]:
        return sorted(self.config.patterns.increments.parse_increments(self.value.lower()))
