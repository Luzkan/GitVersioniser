from abc import ABC, abstractmethod

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.domain.versioniser.utils.versions import Versions


class RoutineVersion(Routine, ABC):
    def run(self) -> Versions:
        return Versions(
            old=self.repo.tags.latest_semver,
            new=self.generate_new_version()
        )

    @abstractmethod
    def generate_new_version(self) -> SemverTag:
        pass
