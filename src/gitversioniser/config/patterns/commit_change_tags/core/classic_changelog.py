from dataclasses import dataclass

from gitversioniser.config.patterns.commit_change_tags.abstract import CommitChangeTags
from gitversioniser.config.patterns.commit_change_tags.changelog_category import ChangelogCategory
from gitversioniser.config.patterns.commit_change_tags.commit_tag import CommitTag


@dataclass(frozen=True)
class ClassicChangelog(CommitChangeTags):
    added: CommitTag = ChangelogCategory.ADDED.value
    fixed: CommitTag = ChangelogCategory.FIXED.value
    changed: CommitTag = ChangelogCategory.CHANGED.value
    removed: CommitTag = ChangelogCategory.REMOVED.value
    security: CommitTag = ChangelogCategory.SECURITY.value
    deprecated: CommitTag = ChangelogCategory.DEPRECATED.value
