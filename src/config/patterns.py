from dataclasses import dataclass

from config.commit_tags import CommitTags
from config.increments import Increments


@dataclass
class Patterns:
    increments: Increments = Increments()
    commit_tags: CommitTags = CommitTags()
