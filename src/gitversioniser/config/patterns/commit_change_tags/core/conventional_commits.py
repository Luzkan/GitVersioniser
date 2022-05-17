from dataclasses import dataclass

from gitversioniser.config.patterns.commit_change_tags.abstract import CommitChangeTags
from gitversioniser.config.patterns.commit_change_tags.commit_tag import CommitTag
from gitversioniser.helpers.changelog_category import ChangelogCategory


@dataclass(frozen=True)
class ConventionalCommits(CommitChangeTags):
    build: CommitTag = CommitTag("Build:", ChangelogCategory.BUILD, "📦")
    ci: CommitTag = CommitTag("CI:", ChangelogCategory.CI, "🪢")
    docs: CommitTag = CommitTag("Docs:", ChangelogCategory.DOCUMENTATION, "📜")
    feature: CommitTag = CommitTag("Feat:", ChangelogCategory.FEATURE, "✨")
    fix: CommitTag = CommitTag("Fix:", ChangelogCategory.FIXED, "🛠️")
    performance: CommitTag = CommitTag("Perf:", ChangelogCategory.PERFORMANCE, "⚡")
    refactored: CommitTag = CommitTag("Refactor:", ChangelogCategory.REFACTORIZATION, "♻️")
    test: CommitTag = CommitTag("Test:", ChangelogCategory.TEST, "🪛")
    chore: CommitTag = CommitTag("Chore:", ChangelogCategory.CHORE, "🧹")
    revert: CommitTag = CommitTag("Revert:", ChangelogCategory.REVERT, "↩️")
    style: CommitTag = CommitTag("Style:", ChangelogCategory.STYLE, "🖌️")
