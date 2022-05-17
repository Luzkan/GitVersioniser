from dataclasses import dataclass

from gitversioniser.config.patterns.commit_change_tags.abstract import CommitChangeTags
from gitversioniser.config.patterns.commit_change_tags.changelog_category import ChangelogCategory
from gitversioniser.config.patterns.commit_change_tags.commit_tag import CommitTag


@dataclass(frozen=True)
class All(CommitChangeTags):
    architecture: CommitTag = ChangelogCategory.ARCHITECTURE.value
    accesibility: CommitTag = ChangelogCategory.ACCESIBILITY.value
    added: CommitTag = ChangelogCategory.ADDED.value
    assets: CommitTag = ChangelogCategory.ASSETS.value
    authorization: CommitTag = ChangelogCategory.AUTH.value
    build: CommitTag = ChangelogCategory.BUILD.value
    breaking: CommitTag = ChangelogCategory.BREAKING_CHANGE.value
    changed: CommitTag = ChangelogCategory.CHANGED.value
    config: CommitTag = ChangelogCategory.CONFIG.value
    ci: CommitTag = ChangelogCategory.CI.value
    chore: CommitTag = ChangelogCategory.CHORE.value
    deprecated: CommitTag = ChangelogCategory.DEPRECATED.value
    deploy: CommitTag = ChangelogCategory.DEPLOY.value
    documentation: CommitTag = ChangelogCategory.DOCUMENTATION.value
    docstring: CommitTag = ChangelogCategory.DOCUMENTATION_DOCSTRING.value
    documentation_formal: CommitTag = ChangelogCategory.DOCUMENTATION_FORMAL.value
    dependency_downgrade: CommitTag = ChangelogCategory.DEPENDENCY_DOWNGRADE.value
    dependency_upgrade: CommitTag = ChangelogCategory.DEPENDENCY_UPGRADE.value
    dependency_added: CommitTag = ChangelogCategory.DEPENDENCY_ADDED.value
    dependency_removed: CommitTag = ChangelogCategory.DEPENDENCY_REMOVED.value
    experimental: CommitTag = ChangelogCategory.EXPERIMENTAL.value
    feature: CommitTag = ChangelogCategory.FEATURE.value
    fixed: CommitTag = ChangelogCategory.FIXED.value
    fixed_hot: CommitTag = ChangelogCategory.FIXED_HOT.value
    fixed_typo: CommitTag = ChangelogCategory.FIXED_TYPO.value
    fixed_tweak: CommitTag = ChangelogCategory.FIXED_SMALL.value
    flag: CommitTag = ChangelogCategory.FLAG.value
    infrastructure: CommitTag = ChangelogCategory.INFRASTRUCTURE.value
    logs_on: CommitTag = ChangelogCategory.LOGS_ON.value
    logs_off: CommitTag = ChangelogCategory.LOGS_OFF.value
    localization: CommitTag = ChangelogCategory.LOCALIZATION.value
    merge_branches: CommitTag = ChangelogCategory.MERGE_BRANCHES.value
    package: CommitTag = ChangelogCategory.PACKAGE.value
    performance: CommitTag = ChangelogCategory.PERFORMANCE.value
    refactorization: CommitTag = ChangelogCategory.REFACTORIZATION.value
    rename: CommitTag = ChangelogCategory.RENAME.value
    revert: CommitTag = ChangelogCategory.REVERT.value
    removed: CommitTag = ChangelogCategory.REMOVED.value
    removed_dead_code: CommitTag = ChangelogCategory.REMOVED_DEAD_CODE.value
    security: CommitTag = ChangelogCategory.SECURITY.value
    seo: CommitTag = ChangelogCategory.SEO.value
    seed: CommitTag = ChangelogCategory.SEED.value
    style: CommitTag = ChangelogCategory.STYLE.value
    usability: CommitTag = ChangelogCategory.USABILITY.value
    text: CommitTag = ChangelogCategory.TEXT.value
    test: CommitTag = ChangelogCategory.TEST.value
    test_failing: CommitTag = ChangelogCategory.TEST_FAILING.value
    tidied: CommitTag = ChangelogCategory.TIDIED.value
    work_in_progress: CommitTag = ChangelogCategory.WORK_IN_PROGRESS.value
