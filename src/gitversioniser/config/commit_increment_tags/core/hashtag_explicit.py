from dataclasses import dataclass

from gitversioniser.config.commit_increment_tags.abstract import CommitIncrementTags
from gitversioniser.config.commit_increment_tags.increment import Increment
from gitversioniser.helpers.version_bump import VersionBump


@dataclass(frozen=True)
class HashtagExplicit(CommitIncrementTags):
    major: Increment = Increment(VersionBump.MAJOR, 1, "#major", lambda version: version.bump_major())
    minor: Increment = Increment(VersionBump.MINOR, 1, "#minor", lambda version: version.bump_minor())
    patch: Increment = Increment(VersionBump.PATCH, 1, "#patch", lambda version: version.bump_patch())
    alpha: Increment = Increment(VersionBump.ALPHA, 2, "#alpha", lambda version: version.bump_prerelease('alpha'))
    beta: Increment = Increment(VersionBump.BETA, 3, "#beta", lambda version: version.bump_prerelease('beta'))
    prerelease: Increment = Increment(VersionBump.PRERELEASE, 4, "#prerelease", lambda version: version.bump_prerelease())
    finalized: Increment = Increment(VersionBump.FINALIZED, 9, "#fin", lambda version: version.finalize_version())
