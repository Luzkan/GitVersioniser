from dataclasses import dataclass

from gitversioniser.config.patterns.commit_increment_tags.increment import Increment
from gitversioniser.domain.repository.commit_utils.tag import TagUtils


@dataclass
class IncrementTagUtils(TagUtils):
    def exist(self) -> bool:
        return self.config.commit_patterns.increment_tags.has_increment(self.value.lower())

    def get(self) -> list[Increment]:
        return sorted(self.config.commit_patterns.increment_tags.parse_increments(self.value.lower()))
