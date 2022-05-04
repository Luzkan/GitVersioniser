from .always import Always
from .if_new_version_is_build_or_higher import IfNewVersionIsBuildOrHigher
from .if_new_version_is_patch_or_higher import IfNewVersionIsPatchOrHigher
from .if_new_version_is_prerelease_or_higher import IfNewVersionIsPrereleaseOrHigher
from .never import Never


__all__ = [
    'Always',
    'IfNewVersionIsBuildOrHigher',
    'IfNewVersionIsPatchOrHigher',
    'IfNewVersionIsPrereleaseOrHigher',
    'Never',
]
