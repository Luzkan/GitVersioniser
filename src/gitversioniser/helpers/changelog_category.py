from enum import Enum


class ChangelogCategory(Enum):
    ADDED = "Added"
    BUILD = "Build"
    CHANGED = "Changed"
    CI = "CI"
    DEPRECATED = "Deprecated"
    DOCUMENTATION = "Documentation"
    FEATURE = "Feature"
    FIXED = "Fixed"
    PERFORMANCE = "Performance"
    REFACTORIZATION = "Refactorization"
    REMOVED = "Removed"
    SECURITY = "Security"
    TEST = "Test"
