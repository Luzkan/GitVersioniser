from dataclasses import dataclass

from gitversioniser.config.patterns.commit_change_tags.abstract import CommitChangeTags
from gitversioniser.config.patterns.commit_change_tags.commit_tag import CommitTag
from gitversioniser.config.patterns.commit_change_tags.changelog_category import ChangelogCategory


@dataclass(frozen=True)
class AngularCommits(CommitChangeTags):
    build: CommitTag = ChangelogCategory.BUILD.value
    ci: CommitTag = ChangelogCategory.CI.value
    docs: CommitTag = ChangelogCategory.DOCUMENTATION.value
    feature: CommitTag = ChangelogCategory.FEATURE.value
    fix: CommitTag = ChangelogCategory.FIXED.value
    performance: CommitTag = ChangelogCategory.PERFORMANCE.value
    refactored: CommitTag = ChangelogCategory.REFACTORIZATION.value
    test: CommitTag = ChangelogCategory.TEST.value
