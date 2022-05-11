from dataclasses import dataclass

from gitversioniser.config.patterns.commit_increment_tags.abstract import CommitIncrementTags
from gitversioniser.config.patterns.commit_increment_tags.increment import Increment


@dataclass(frozen=True)
class HashtagExplicit(CommitIncrementTags):
    major: Increment = Increment(1, "#major", lambda version: version.bump_major())
    minor: Increment = Increment(1, "#minor", lambda version: version.bump_minor())
    patch: Increment = Increment(1, "#patch", lambda version: version.bump_patch())
    alpha: Increment = Increment(2, "#alpha", lambda version: version.bump_prerelease('alpha'))
    beta: Increment = Increment(3, "#beta", lambda version: version.bump_prerelease('beta'))
    prerelease: Increment = Increment(4, "#prerelease", lambda version: version.bump_prerelease())
    finalized: Increment = Increment(9, "#fin", lambda version: version.finalize_version())
