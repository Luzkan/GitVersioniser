from dataclasses import dataclass

from gitversioniser.config.commit_change_tags import ClassicChangelog, CommitChangeTags
from gitversioniser.config.commit_increment_tags import CommitIncrementTags, HashtagExplicit


@dataclass(frozen=True)
class Patterns:
    increments: CommitIncrementTags = HashtagExplicit()
    commit_tags: CommitChangeTags = ClassicChangelog()
