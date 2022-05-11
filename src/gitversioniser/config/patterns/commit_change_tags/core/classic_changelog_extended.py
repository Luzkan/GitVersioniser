from dataclasses import dataclass

from gitversioniser.config.patterns.commit_change_tags.abstract import CommitChangeTags
from gitversioniser.config.patterns.commit_change_tags.commit_tag import CommitTag
from gitversioniser.helpers.changelog_category import ChangelogCategory


@dataclass(frozen=True)
class ClassicChangelogExtended(CommitChangeTags):
    test: CommitTag = CommitTag("T:", ChangelogCategory.TEST, "🪛")
    added: CommitTag = CommitTag("A:", ChangelogCategory.ADDED, "💠")
    fixed: CommitTag = CommitTag("F:", ChangelogCategory.FIXED, "🛠️")
    changed: CommitTag = CommitTag("C:", ChangelogCategory.CHANGED, "🔸")
    removed: CommitTag = CommitTag("R:", ChangelogCategory.REMOVED, "🗑️")
    tidied: CommitTag = CommitTag("TIDY:", ChangelogCategory.TIDIED, "🧹")
    refactored: CommitTag = CommitTag("REF:", ChangelogCategory.REFACTORIZATION, "♻️")
    security: CommitTag = CommitTag("SEC:", ChangelogCategory.SECURITY, "🔐")
    performance: CommitTag = CommitTag("PERF:", ChangelogCategory.PERFORMANCE, "⚡")
    deprecated: CommitTag = CommitTag("DEP:", ChangelogCategory.DEPRECATED, "🔚")
    documentation: CommitTag = CommitTag("DOC:", ChangelogCategory.DOCUMENTATION, "📜")
