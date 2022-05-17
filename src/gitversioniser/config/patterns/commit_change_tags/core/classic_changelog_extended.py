from dataclasses import dataclass

from gitversioniser.config.patterns.commit_change_tags.abstract import CommitChangeTags
from gitversioniser.config.patterns.commit_change_tags.commit_tag import CommitTag
from gitversioniser.config.patterns.commit_change_tags.changelog_category import ChangelogCategory


@dataclass(frozen=True)
class ClassicChangelogExtended(CommitChangeTags):
    ci: CommitTag = ChangelogCategory.CI.value
    test: CommitTag = ChangelogCategory.TEST.value
    added: CommitTag = ChangelogCategory.ADDED.value
    fixed: CommitTag = ChangelogCategory.FIXED.value
    changed: CommitTag = ChangelogCategory.CHANGED.value
    removed: CommitTag = ChangelogCategory.REMOVED.value
    tidied: CommitTag = ChangelogCategory.TIDIED.value
    refactored: CommitTag = ChangelogCategory.REFACTORIZATION.value
    security: CommitTag = ChangelogCategory.SECURITY.value
    performance: CommitTag = ChangelogCategory.PERFORMANCE.value
    deprecated: CommitTag = ChangelogCategory.DEPRECATED.value
    documentation: CommitTag = ChangelogCategory.DOCUMENTATION.value
