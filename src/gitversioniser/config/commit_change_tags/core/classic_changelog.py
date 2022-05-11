from dataclasses import dataclass

from gitversioniser.config.commit_change_tags.abstract import CommitChangeTags
from gitversioniser.config.commit_change_tags.commit_tag import CommitTag
from gitversioniser.helpers.changelog_category import ChangelogCategory


@dataclass(frozen=True)
class ClassicChangelog(CommitChangeTags):
    added: CommitTag = CommitTag("A:", ChangelogCategory.ADDED, "💠")
    fixed: CommitTag = CommitTag("F:", ChangelogCategory.FIXED, "🛠️")
    changed: CommitTag = CommitTag("C:", ChangelogCategory.CHANGED, "🔸")
    removed: CommitTag = CommitTag("R:", ChangelogCategory.REMOVED, "🗑️")
    security: CommitTag = CommitTag("S:", ChangelogCategory.SECURITY, "🔐")
    deprecated: CommitTag = CommitTag("D:", ChangelogCategory.DEPRECATED, "🔚")
