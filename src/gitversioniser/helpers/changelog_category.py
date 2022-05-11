from enum import Enum


class ChangelogCategory(Enum):
    ADDED = "Added"
    BUILD = "Build"
    CHANGED = "Changed"
    CI = "CI"
    CHORE = "Chore"
    DEPRECATED = "Deprecated"
    DOCUMENTATION = "Documentation"
    FEATURE = "Feature"
    FIXED = "Fixed"
    PERFORMANCE = "Performance"
    REFACTORIZATION = "Refactorization"
    REVERT = "Revert"
    REMOVED = "Removed"
    SECURITY = "Security"
    STYLE = "Style"
    TEST = "Test"
    TIDIED = "Tidied"
