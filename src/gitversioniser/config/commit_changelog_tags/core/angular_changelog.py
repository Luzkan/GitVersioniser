from dataclasses import dataclass

from gitversioniser.config.commit_changelog_tags.abstract import CommitChangelogTags
from gitversioniser.config.commit_changelog_tags.commit_tag import CommitTag
from gitversioniser.helpers.changelog_category import ChangelogCategory


@dataclass(frozen=True)
class AngularChangelog(CommitChangelogTags):
    build: CommitTag = CommitTag("Build:", ChangelogCategory.BUILD)
    ci: CommitTag = CommitTag("CI:", ChangelogCategory.CI)
    docs: CommitTag = CommitTag("Docs:", ChangelogCategory.DOCUMENTATION)
    feature: CommitTag = CommitTag("Feat:", ChangelogCategory.FEATURE)
    fix: CommitTag = CommitTag("Fix:", ChangelogCategory.FIXED)
    performance: CommitTag = CommitTag("Perf:", ChangelogCategory.PERFORMANCE)
    refactorization: CommitTag = CommitTag("Refactor:", ChangelogCategory.REFACTORIZATION)
    test: CommitTag = CommitTag("Test:", ChangelogCategory.TEST)
