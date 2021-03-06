from enum import Enum

from gitversioniser.config.patterns.commit_change_tags.commit_tag import CommitTag


class ChangelogCategory(Enum):
    ARCHITECTURE = CommitTag(
        "Architecture", "Arch:", "๐๏ธ",
        ["Arch:", "Architecture:"]
    )
    ACCESIBILITY = CommitTag(
        "Accessibility", "Accessibility:", "โฟ๏ธ",
        ["Accessibility:"]
    )
    ADDED = CommitTag(
        "Added", "A:", "โจ",
        ["A:", "Add:", "Added:", "Addition:", "Additions:"]
    )
    ASSETS = CommitTag(
        "Assets", "Assets:", "๐ฑ",
        ["Assets", "Assets:"]
    )
    AUTH = CommitTag(
        "Authorization", "Auth:", "๐",
        ["Auth:", "Authorization:"]
    )
    BUILD = CommitTag(
        "Build", "B:", "๐ฆ",
        ["B:", "Build:", "Builds:"]
    )
    BREAKING_CHANGE = CommitTag(
        "Breaking Change", "Break:", "๐ฅ",
        ["Breaking:", "Breaking:"]
    )
    CHANGED = CommitTag(
        "Changed", "C:", "๐จ",
        ["C:", "Change:", "Changes:", "Changed:"]
    )
    CONFIG = CommitTag(
        "Configuration", "CFG:", "๐ง",
        ["CFG:", "Config:", "Configs:"]
    )
    CI = CommitTag(
        "Continuous Integration", "CI:", "๐ชข",
        ["CI:", "Continuous:", "Continuous Integration:"]
    )
    CHORE = CommitTag(
        "Chore", "C:", "๐งน",
        ["C:", "Chore:", "Chores:"]
    )
    DATABASE = CommitTag(
        "Database", "DB:", "๐๏ธ",
        ["DB:", "Database:"]
    )
    DEPRECATED = CommitTag(
        "Deprecated", "Dep:", "๐",
        ["Dep:", "Deprecated:", "Deprecation:", "Deprecations:"]
    )
    DEPLOY = CommitTag(
        "Deploy", "Deploy:", "๐",
        ["Deploy:", "Deploys:", "Deployed:"]
    )
    DOCUMENTATION = CommitTag(
        "Documentation", "Doc:", "๐",
        ["Doc:", "Documentation:"]
    )
    DOCUMENTATION_DOCSTRING = CommitTag(
        "Docstring", "Docstring:", "๐",
        ["Docstring:"]
    )
    DOCUMENTATION_FORMAL = CommitTag(
        "Formal Documentation", "FDoc:", "๐",
        ["FDoc:", "Formal:", "Formal Documentation:"]
    )
    DEPENDENCY_DOWNGRADE = CommitTag(
        "Dependency Downgrade", "Dep. Down:", "โฌ๏ธ",
        ["DPNDC Down:", "Dep Down:", "Dep, Down:", "Dependency Downgrade:", "Dependency Downgrades:"]
    )
    DEPENDENCY_UPGRADE = CommitTag(
        "Dependency Upgrade", "Dep. Up:", "โฌ๏ธ",
        ["DPNDC Up:", "Dep Up:", "Dep. Up:", "Dependency Upgrade:", "Dependency Upgrades:"]
    )
    DEPENDENCY_ADDED = CommitTag(
        "Dependency Added", "Dep. Added:", "โ",
        ["DPNDC Added:", "Dep Added:", "Dep. Added:", "Dependency Added:", "Dependency Added:"]
    )
    DEPENDENCY_REMOVED = CommitTag(
        "Dependency Removed", "Dep. Removed:", "โ",
        ["DPNDC Removed:", "Dep Removed:", "Dep. Removed:", "Dependency Removed:", "Dependency Removed:"]
    )
    EXPERIMENTAL = CommitTag(
        "Experimental", "Exp:", "โ๏ธ",
        ["Exp:", "Experimental:"]
    )
    FEATURE = CommitTag(
        "Feature", "Feat:", "๐",
        ["Feat:", "Feature:", "Features:"]
    )
    FIXED = CommitTag(
        "Fixed", "F:", "๐?๏ธ",
        ["F:", "Fix:", "Fixes:", "Fixed:"]
    )
    FIXED_BUG = CommitTag(
        "Bugfix", "Bug:", "๐",
        ["Bug:", "Bugfix:", "Bugfixes:", "Bugfix:", "Bugfixes:"]
    )
    FIXED_HOT = CommitTag(
        "Hotfix", "HF:", "๐๏ธ",
        ["HF:", "Hotfix:", "Hotfixes:", "Hot Fix:", "Hot Fixes:", "Hot Fixed:"]
    )
    FIXED_TYPO = CommitTag(
        "Typo", "Typo:", "โ๏ธ",
        ["Typo:", "TF:"]
    )
    FIXED_SMALL = CommitTag(
        "Tweak", "Tweak:", "๐ฉน",
        ["FT:", "Fix Tweak:", "Tweaks:", "Tweak:", "Small Fix:", "Quick Fix:"]
    )
    FLAG = CommitTag(
        "Feature Flag", "Flag:", "๐ฉ",
        ["Flag:", "Feature Flags:", "Feature Flag:"]
    )
    IGNORE = CommitTag(
        "Ignore", "Ignore:", "๐",
        ["Ignore:", "Ignores:", "Gitignore:", "Git Ignore:"]
    )
    INFRASTRUCTURE = CommitTag(
        "Infrastructure", "I:", "๐งฑ",
        ["I:", "Infrastructure:", "Structure:"]
    )
    LOGS_ON = CommitTag(
        "Added Logging", "Logs ON:", "๐",
        ["Logs ON:", "Logging:", "Log:", "Logs:"]
    )
    LOGS_OFF = CommitTag(
        "Added Logging", "Logs OFF:", "๐",
        ["Logs OFF:"]
    )
    LOCALIZATION = CommitTag(
        "Localization", "Locale:", "๐",
        ["Locale:", "Localization:", "Lang:", "Language:"]
    )
    MERGE_BRANCHES = CommitTag(
        "Merge Branches", "Merged:", "๐",
        ["Merge pull"]
    )
    MOBILE = CommitTag(
        "Mobile", "Mobile:", "๐ฑ",
        ["Mobile:"]
    )
    PACKAGE = CommitTag(
        "Dependencies", "Package:", "๐ฆ๏ธ",
        ["Package:"]
    )
    PERFORMANCE = CommitTag(
        "Performance", "Perf:", "โก",
        ["Perf:", "Performance:"]
    )
    REFACTORIZATION = CommitTag(
        "Refactored", "Ref:", "โป๏ธ",
        ["Ref:", "Refactor:", "Refactoring:", "Refactored:"]
    )
    RENAME = CommitTag(
        "Rename", "Rename:", "๐",
        ["Rename:", "Renamed:", "Renames:"]
    )
    REVERT = CommitTag(
        "Revert", "Revert", "๐",
        ["Reverted:", "Revert:"]
    )
    REMOVED = CommitTag(
        "Removed", "R:", "๐๏ธ",
        ["R:", "Remove:", "Removed:", "Removal:"]
    )
    REMOVED_DEAD_CODE = CommitTag(
        "Removed Dead Code", "Dead:", "โฐ๏ธ",
        ["Dead:", "Dead Code:", "Removed Dead Code:"]
    )
    SECURITY = CommitTag(
        "Security", "Sec:", "๐",
        ["Sec:", "Security:"]
    )
    SEO = CommitTag(
        "SEO", "SEO:", "๐๏ธ",
        ["SEO", "SEO:"]
    )
    SEED = CommitTag(
        "Seed", "Seed:", "๐ฑ",
        ["Seed:"]
    )
    STYLE = CommitTag(
        "Style", "Style:", "๐จ",
        ["Style:", "Formatting:"]
    )
    SNAPSHOT = CommitTag(
        "Snapshot", "Snap:", "๐ธ",
        ["Snap:", "Snapshot:", "Snapshots:"]
    )
    USABILITY = CommitTag(
        "Usability", "U:", "๐ธ",
        ["U:", "Usability:"]
    )
    TEXT = CommitTag(
        "Lexical", "Text:", "๐ฌ",
        ["Text:", "Lexical:"]
    )
    TEST = CommitTag(
        "Test", "T:", "โ",
        ["T:", "Test:"]
    )
    TEST_FAILING = CommitTag(
        "Failing Test", "TFail:", "๐งช",
        ["FT:", "TFail:", "Failing Test:"]
    )
    TIDIED = CommitTag(
        "Tidied", "Tidy:", "๐งน",
        ["Tidy:", "Tidied:", "Tidying:"]
    )
    VERSION = CommitTag(
        "Version", "V:", "๐",
        ["V:", "Version:", "Versions:"]
    )
    WORK_IN_PROGRESS = CommitTag(
        "Work in Progress", "WIP:", "๐ง",
        ["WIP:", "Work in Progress:"]
    )
