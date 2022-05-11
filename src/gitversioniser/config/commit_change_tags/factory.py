from gitversioniser.config.commit_change_tags.abstract import CommitChangeTags
from gitversioniser.config.commit_change_tags.core import AngularCommits, ClassicChangelog, ClassicChangelogExtended, ConventionalCommits
from gitversioniser.helpers.types import COMMIT_CHANGE_TAG_TYPE


class CommitChangeTagsFactory:
    @staticmethod
    def create(routine: COMMIT_CHANGE_TAG_TYPE) -> type[CommitChangeTags]:
        return {
            'AngularCommits': AngularCommits,
            'ClassicChangelog': ClassicChangelog,
            'ClassicChangelogExtended': ClassicChangelogExtended,
            'ConventionalCommits': ConventionalCommits
        }[routine]
