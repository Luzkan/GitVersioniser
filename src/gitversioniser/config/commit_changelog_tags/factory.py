from gitversioniser.config.commit_changelog_tags.abstract import CommitChangelogTags
from gitversioniser.config.commit_changelog_tags.core.classic_changelog import ClassicChangelog
from gitversioniser.helpers.types import COMMIT_CHANGELOG_TAG_TYPE


class CommitChangelogTagsFactory:
    @staticmethod
    def create(routine: COMMIT_CHANGELOG_TAG_TYPE) -> type[CommitChangelogTags]:
        return {
            'ClassicChangelog': ClassicChangelog,
        }[routine]
