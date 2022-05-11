from dataclasses import dataclass

from gitversioniser.config.patterns.commit_change_tags import ClassicChangelog, CommitChangeTags
from gitversioniser.config.patterns.commit_change_tags.factory import CommitChangeTagsFactory
from gitversioniser.config.patterns.commit_increment_tags import CommitIncrementTags, HashtagExplicit
from gitversioniser.config.patterns.commit_increment_tags.factory import CommitIncrementTagsFactory
from gitversioniser.helpers.types import COMMIT_CHANGE_TAG_TYPE, COMMIT_INCREMENT_TAG_TYPE


@dataclass(frozen=True)
class CommitPatterns:
    increment_tags: CommitIncrementTags = HashtagExplicit()
    change_tags: CommitChangeTags = ClassicChangelog()

    @staticmethod
    def init_from_arguments(increment_tags: COMMIT_INCREMENT_TAG_TYPE, change_tags: COMMIT_CHANGE_TAG_TYPE) -> 'CommitPatterns':
        return CommitPatterns(
            increment_tags=CommitIncrementTagsFactory.create(increment_tags)(),
            change_tags=CommitChangeTagsFactory.create(change_tags)(),
        )
