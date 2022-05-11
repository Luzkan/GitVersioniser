from gitversioniser.config.patterns.commit_increment_tags.abstract import CommitIncrementTags
from gitversioniser.config.patterns.commit_increment_tags.core.hashtag_explicit import HashtagExplicit
from gitversioniser.helpers.types import COMMIT_INCREMENT_TAG_TYPE


class CommitIncrementTagsFactory:
    @staticmethod
    def create(routine: COMMIT_INCREMENT_TAG_TYPE) -> type[CommitIncrementTags]:
        return {
            'HashtagExplicit': HashtagExplicit,
        }[routine]
