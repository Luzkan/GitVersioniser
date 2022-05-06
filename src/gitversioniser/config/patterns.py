from dataclasses import dataclass

from gitversioniser.config.commit_tags import CommitTags
from gitversioniser.config.increments import Increments


@dataclass(frozen=True)
class Patterns:
    increments: Increments = Increments()
    commit_tags: CommitTags = CommitTags()
