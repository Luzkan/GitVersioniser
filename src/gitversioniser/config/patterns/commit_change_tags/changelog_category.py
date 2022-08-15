from enum import Enum

from gitversioniser.config.patterns.commit_change_tags.commit_tag import CommitTag


class ChangelogCategory(Enum):
    ARCHITECTURE = CommitTag(
        "Architecture", "Arch:", "🏗️",
        ["Arch:", "Architecture:"]
    )
    ACCESIBILITY = CommitTag(
        "Accessibility", "Accessibility:", "♿️",
        ["Accessibility:"]
    )
    ADDED = CommitTag(
        "Added", "A:", "✨",
        ["A:", "Add:", "Added:", "Addition:", "Additions:"]
    )
    ASSETS = CommitTag(
        "Assets", "Assets:", "🍱",
        ["Assets", "Assets:"]
    )
    AUTH = CommitTag(
        "Authorization", "Auth:", "🛂",
        ["Auth:", "Authorization:"]
    )
    BUILD = CommitTag(
        "Build", "B:", "📦",
        ["B:", "Build:", "Builds:"]
    )
    BREAKING_CHANGE = CommitTag(
        "Breaking Change", "Break:", "💥",
        ["Breaking:", "Breaking:"]
    )
    CHANGED = CommitTag(
        "Changed", "C:", "🔨",
        ["C:", "Change:", "Changes:", "Changed:"]
    )
    CONFIG = CommitTag(
        "Configuration", "CFG:", "🔧",
        ["CFG:", "Config:", "Configs:"]
    )
    CI = CommitTag(
        "Continuous Integration", "CI:", "🪢",
        ["CI:", "Continuous:", "Continuous Integration:"]
    )
    CHORE = CommitTag(
        "Chore", "C:", "🧹",
        ["C:", "Chore:", "Chores:"]
    )
    DATABASE = CommitTag(
        "Database", "DB:", "🗃️",
        ["DB:", "Database:"]
    )
    DEPRECATED = CommitTag(
        "Deprecated", "Dep:", "🔚",
        ["Dep:", "Deprecated:", "Deprecation:", "Deprecations:"]
    )
    DEPLOY = CommitTag(
        "Deploy", "Deploy:", "🚀",
        ["Deploy:", "Deploys:", "Deployed:"]
    )
    DOCUMENTATION = CommitTag(
        "Documentation", "Doc:", "📝",
        ["Doc:", "Docs:", "Documentation:"]
    )
    DOCUMENTATION_DOCSTRING = CommitTag(
        "Docstring", "Docstring:", "📜",
        ["Docstring:"]
    )
    DOCUMENTATION_FORMAL = CommitTag(
        "Formal Documentation", "FDoc:", "📄",
        ["FDoc:", "Formal:", "Formal Documentation:"]
    )
    DEPENDENCY_DOWNGRADE = CommitTag(
        "Dependency Downgrade", "Dep. Down:", "⬇️",
        ["DPNDC Down:", "Dep Down:", "Dep, Down:", "Dependency Downgrade:", "Dependency Downgrades:"]
    )
    DEPENDENCY_UPGRADE = CommitTag(
        "Dependency Upgrade", "Dep. Up:", "⬆️",
        ["DPNDC Up:", "Dep Up:", "Dep. Up:", "Dependency Upgrade:", "Dependency Upgrades:"]
    )
    DEPENDENCY_ADDED = CommitTag(
        "Dependency Added", "Dep. Added:", "➕",
        ["DPNDC Added:", "Dep Added:", "Dep. Added:", "Dependency Added:", "Dependency Added:"]
    )
    DEPENDENCY_REMOVED = CommitTag(
        "Dependency Removed", "Dep. Removed:", "➖",
        ["DPNDC Removed:", "Dep Removed:", "Dep. Removed:", "Dependency Removed:", "Dependency Removed:"]
    )
    EXPERIMENTAL = CommitTag(
        "Experimental", "Exp:", "⚗️",
        ["Exp:", "Experimental:"]
    )
    FEATURE = CommitTag(
        "Feature", "Feat:", "🎉",
        ["Feat:", "Feature:", "Features:"]
    )
    FIXED = CommitTag(
        "Fixed", "F:", "🛠️",
        ["F:", "Fix:", "Fixes:", "Fixed:"]
    )
    FIXED_BUG = CommitTag(
        "Bugfix", "Bug:", "🐛",
        ["Bug:", "Bugfix:", "Bugfixes:", "Bugfix:", "Bugfixes:"]
    )
    FIXED_HOT = CommitTag(
        "Hotfix", "HF:", "🚑️",
        ["HF:", "Hotfix:", "Hotfixes:", "Hot Fix:", "Hot Fixes:", "Hot Fixed:"]
    )
    FIXED_TYPO = CommitTag(
        "Typo", "Typo:", "✏️",
        ["Typo:", "TF:"]
    )
    FIXED_SMALL = CommitTag(
        "Tweak", "Tweak:", "🩹",
        ["FT:", "Fix Tweak:", "Tweaks:", "Tweak:", "Small Fix:", "Quick Fix:"]
    )
    FLAG = CommitTag(
        "Feature Flag", "Flag:", "🚩",
        ["Flag:", "Feature Flags:", "Feature Flag:"]
    )
    IGNORE = CommitTag(
        "Ignore", "Ignore:", "🙈",
        ["Ignore:", "Ignores:", "Gitignore:", "Git Ignore:"]
    )
    LOGS_ON = CommitTag(
        "Added Logging", "Logs ON:", "🔊",
        ["Logs ON:", "Logging:", "Log:", "Logs:"]
    )
    LOGS_OFF = CommitTag(
        "Added Logging", "Logs OFF:", "🔇",
        ["Logs OFF:"]
    )
    LOCALIZATION = CommitTag(
        "Localization", "Locale:", "🌐",
        ["Locale:", "Localization:", "Lang:", "Language:"]
    )
    MERGE_BRANCHES = CommitTag(
        "Merge Branches", "Merged:", "🔀",
        ["Merge pull"]
    )
    MOBILE = CommitTag(
        "Mobile", "Mobile:", "📱",
        ["Mobile:"]
    )
    PACKAGE = CommitTag(
        "Dependencies", "Package:", "📦️",
        ["Package:"]
    )
    PERFORMANCE = CommitTag(
        "Performance", "Perf:", "⚡",
        ["Perf:", "Performance:"]
    )
    REFACTORIZATION = CommitTag(
        "Refactored", "Ref:", "♻️",
        ["Ref:", "Refactor:", "Refactoring:", "Refactored:"]
    )
    RENAME = CommitTag(
        "Rename", "Rename:", "🚚",
        ["Rename:", "Renamed:", "Renames:"]
    )
    REVERT = CommitTag(
        "Revert", "Revert", "🔙",
        ["Reverted:", "Revert:"]
    )
    REMOVED = CommitTag(
        "Removed", "R:", "🗑️",
        ["R:", "Remove:", "Removed:", "Removal:"]
    )
    REMOVED_DEAD_CODE = CommitTag(
        "Removed Dead Code", "Dead:", "⚰️",
        ["Dead:", "Dead Code:", "Removed Dead Code:"]
    )
    SECURITY = CommitTag(
        "Security", "Sec:", "🔐",
        ["Sec:", "Security:"]
    )
    SEO = CommitTag(
        "SEO", "SEO:", "🔍️",
        ["SEO", "SEO:"]
    )
    SEED = CommitTag(
        "Seed", "Seed:", "🌱",
        ["Seed:"]
    )
    STRUCTURE = CommitTag(
        "Structure", "S:", "🏰",
        ["S:", "Structure:", "Infrastructure:"]
    )
    STYLE = CommitTag(
        "Style", "Style:", "🎨",
        ["Style:", "Formatting:"]
    )
    SNAPSHOT = CommitTag(
        "Snapshot", "Snap:", "📸",
        ["Snap:", "Snapshot:", "Snapshots:"]
    )
    USABILITY = CommitTag(
        "Usability", "U:", "🚸",
        ["U:", "Usability:"]
    )
    TEXT = CommitTag(
        "Lexical", "Text:", "💬",
        ["Text:", "Lexical:"]
    )
    TEST = CommitTag(
        "Test", "T:", "✅",
        ["T:", "Test:"]
    )
    TEST_FAILING = CommitTag(
        "Failing Test", "TFail:", "🧪",
        ["FT:", "TFail:", "Failing Test:"]
    )
    TIDIED = CommitTag(
        "Tidied", "Tidy:", "🧹",
        ["Tidy:", "Tidied:", "Tidying:"]
    )
    VERSION = CommitTag(
        "Version", "V:", "🔖",
        ["V:", "Version:", "Versions:"]
    )
    WORK_IN_PROGRESS = CommitTag(
        "Work in Progress", "WIP:", "🚧",
        ["WIP:", "Work in Progress:"]
    )
