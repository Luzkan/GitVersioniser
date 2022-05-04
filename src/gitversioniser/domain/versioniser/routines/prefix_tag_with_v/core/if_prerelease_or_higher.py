from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.version_comparer import VersionComparer
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.abstract import RoutinePrefixTagWithV
from gitversioniser.domain.versioniser.utils.versions import Versions


@dataclass
class IfPrereleaseOrHigher(RoutinePrefixTagWithV):
    def run(self, versions: Versions) -> bool:
        version_comparer = VersionComparer(versions)
        return any([
            version_comparer.is_new_major(),
            version_comparer.is_new_minor(),
            version_comparer.is_new_patch(),
            version_comparer.is_new_prerelease()
        ])
