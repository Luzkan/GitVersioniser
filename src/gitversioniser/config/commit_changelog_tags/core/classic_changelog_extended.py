from dataclasses import dataclass

from gitversioniser.config.commit_changelog_tags.abstract import CommitChangelogTags
from gitversioniser.config.commit_changelog_tags.commit_tag import CommitTag
from gitversioniser.helpers.changelog_category import ChangelogCategory


@dataclass(frozen=True)
class ExtendedChangelog(CommitChangelogTags):
    test: CommitTag = CommitTag("T:", ChangelogCategory.TEST)
    added: CommitTag = CommitTag("A:", ChangelogCategory.ADDED)
    fixed: CommitTag = CommitTag("F:", ChangelogCategory.FIXED)
    changed: CommitTag = CommitTag("C:", ChangelogCategory.CHANGED)
    removed: CommitTag = CommitTag("RM:", ChangelogCategory.REMOVED)
    refactor: CommitTag = CommitTag("R:", ChangelogCategory.REFACTORIZATION)
    security: CommitTag = CommitTag("S:", ChangelogCategory.SECURITY)
    performance: CommitTag = CommitTag("P:", ChangelogCategory.PERFORMANCE)
    deprecated: CommitTag = CommitTag("DEP:", ChangelogCategory.DEPRECATED)
    documentation: CommitTag = CommitTag("DOC:", ChangelogCategory.DOCUMENTATION)
