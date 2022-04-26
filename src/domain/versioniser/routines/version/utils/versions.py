from dataclasses import dataclass

from semver import VersionInfo


@dataclass
class Versions:
    old: VersionInfo
    new: VersionInfo
