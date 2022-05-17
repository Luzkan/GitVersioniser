from gitversioniser.config.patterns.commit_change_tags.abstract import CommitChangeTags
from gitversioniser.config.patterns.commit_change_tags.core import (
    All,
    AngularCommits,
    ClassicChangelog,
    ClassicChangelogExtended,
    ConventionalCommits,
)
from gitversioniser.helpers.types import COMMIT_CHANGE_TAG_TYPE


class CommitChangeTagsFactory:
    @staticmethod
    def create(routine: COMMIT_CHANGE_TAG_TYPE) -> type[CommitChangeTags]:
        return {
            'All': All,
            'AngularCommits': AngularCommits,
            'ClassicChangelog': ClassicChangelog,
            'ClassicChangelogExtended': ClassicChangelogExtended,
            'ConventionalCommits': ConventionalCommits
        }[routine]
