from enum import Enum


class VersionBump(Enum):
    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"
    ALPHA = "alpha"
    BETA = "beta"
    PRERELEASE = "prerelease"
    FINALIZED = "finalized"
