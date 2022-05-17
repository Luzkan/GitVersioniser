from enum import Enum

from gitversioniser.config.patterns.commit_change_tags.commit_tag import CommitTag


class ChangelogCategory(Enum):
    ADDED = CommitTag(
        "Added", "A:", "✨",
        ["A:", "Add:", "Added", "Added:", "Addition:", "Additions:", "Addition", "Additions"]
    )
    BUILD = CommitTag(
        "Build", "B:", "📦",
        ["B:", "Build:", "Builds:", "Builds", "Build"]
    )
    CHANGED = CommitTag(
        "Changed", "C:", "🔸",
        ["C:", "Change:", "Changes:", "Changes", "Change", "Changed", "Changed:"]
    )
    CI = CommitTag(
        "Continuous Integration", "CI:", "🪢",
        ["CI:", "Continuous:", "Continuous Integration:", "Continuous Integration", "Continuous"]
    )
    CHORE = CommitTag(
        "Chore", "C:", "🧹",
        ["C:", "Chore:", "Chores:", "Chores", "Chore"]
    )
    DEPRECATED = CommitTag(
        "Deprecated", "Dep:", "🔚",
        ["Dep:", "Deprecated:", "Deprecation:", "Deprecation", "Deprecations:", "Deprecations"]
    )
    DOCUMENTATION = CommitTag(
        "Documentation", "Doc:", "📜",
        ["Doc:", "Documentation:", "Documentation", "Documentation:", "Documentation"]
    )
    FEATURE = CommitTag(
        "Feature", "F:", "🎉",
        ["F:", "Feature:", "Features:", "Features", "Feature"]
    )
    FIXED = CommitTag(
        "Fixed", "F:", "🛠️",
        ["F:", "Fix:", "Fixed", "Fixes:", "Fixes"]
    )
    PERFORMANCE = CommitTag(
        "Performance", "Perf:", "⚡",
        ["Perf:", "Performance:", "Performance"]
    )
    REFACTORIZATION = CommitTag(
        "Refactored", "Ref:", "♻️",
        ["Ref:", "Refactor:", "Refactored", "Refactoring:", "Refactoring"]
    )
    REVERT = CommitTag(
        "Revert", "Revert", "🔙",
        ["Revert", "Revert:"]
    )
    REMOVED = CommitTag(
        "Removed", "R:", "🗑️",
        ["R:", "Remove:", "Removed", "Removal:", "Removal"]
    )
    SECURITY = CommitTag(
        "Security", "Sec:", "🔐",
        ["Sec:", "Security:", "Security"]
    )
    STYLE = CommitTag(
        "Style", "Style:", "🎨",
        ["Style:", "Style"]
    )
    TEST = CommitTag(
        "Test", "T:", "🪛",
        ["T:", "Test:", "Test"]
    )
    TIDIED = CommitTag(
        "Tidied", "Tidy:", "🧹",
        ["Tidy:", "Tidy", "Tidied", "Tidying"]
    )
