from dataclasses import dataclass

from gitversioniser.domain.repository.semver_tag_utils.comparator import SemverTagComparer
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.abstract import RoutinePrefixTagWithV
from gitversioniser.domain.versioniser.utils.versions import Versions


@dataclass
class IfNewVersionIsPrereleaseOrHigher(RoutinePrefixTagWithV):
    def run(self, versions: Versions) -> bool:
        version_comparer = SemverTagComparer(versions)
        return any([
            version_comparer.is_new_major(),
            version_comparer.is_new_minor(),
            version_comparer.is_new_patch(),
            version_comparer.is_new_prerelease()
        ])
