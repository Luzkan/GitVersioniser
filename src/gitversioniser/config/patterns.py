from dataclasses import dataclass

from gitversioniser.config.commit_changelog_tags import ClassicChangelog, CommitChangelogTags
from gitversioniser.config.commit_increment_tags import CommitIncrementTags, HashtagExplicit


@dataclass(frozen=True)
class Patterns:
    increments: CommitIncrementTags = HashtagExplicit()
    commit_tags: CommitChangelogTags = ClassicChangelog()
