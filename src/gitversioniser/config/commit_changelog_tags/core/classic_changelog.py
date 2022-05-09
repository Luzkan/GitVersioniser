from dataclasses import dataclass

from gitversioniser.config.commit_changelog_tags.abstract import CommitChangelogTags
from gitversioniser.config.commit_changelog_tags.commit_tag import CommitTag
from gitversioniser.helpers.changelog_category import ChangelogCategory


@dataclass(frozen=True)
class ClassicChangelog(CommitChangelogTags):
    added: CommitTag = CommitTag("A:", ChangelogCategory.ADDED)
    fixed: CommitTag = CommitTag("F:", ChangelogCategory.FIXED)
    changed: CommitTag = CommitTag("C:", ChangelogCategory.CHANGED)
    removed: CommitTag = CommitTag("R:", ChangelogCategory.REMOVED)
    security: CommitTag = CommitTag("S:", ChangelogCategory.SECURITY)
    deprecated: CommitTag = CommitTag("D:", ChangelogCategory.DEPRECATED)
