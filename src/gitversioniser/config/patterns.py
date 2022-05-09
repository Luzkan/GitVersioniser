from dataclasses import dataclass

from gitversioniser.config.commit_changelog_tags.abstract import CommitChangelogTags
from gitversioniser.config.commit_changelog_tags.core.classic_changelog import ClassicChangelog
from gitversioniser.config.commit_increment_tags.abstract import CommitIncrementTags


@dataclass(frozen=True)
class Patterns:
    increments: CommitIncrementTags = CommitIncrementTags()
    commit_tags: CommitChangelogTags = ClassicChangelog()
