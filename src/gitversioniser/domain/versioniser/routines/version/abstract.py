from abc import ABC, abstractmethod
from typing import Callable

from semver import VersionInfo

from gitversioniser.domain.versioniser.helpers.versions import Versions
from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.helpers.version_bump import VersionBump


class RoutineVersion(Routine, ABC):
    def run(self) -> Versions:
        return Versions(
            old=self.target_repo.tags.latest_semver,
            new=self.generate_new_version()
        )

    @abstractmethod
    def generate_new_version(self) -> VersionInfo:
        pass

    def default_bump_mapping(self, version: VersionInfo) -> dict[VersionBump, Callable[..., VersionInfo]]:
        return {
            VersionBump.MAJOR: lambda: version.bump_major(),
            VersionBump.MINOR: lambda: version.bump_minor(),
            VersionBump.PATCH: lambda: version.bump_patch()
        }
