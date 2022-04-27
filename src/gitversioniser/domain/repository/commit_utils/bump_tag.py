from dataclasses import dataclass

from gitversioniser.domain.repository.commit_utils.tag import TagUtils
from gitversioniser.helpers.version_bump import VersionBump


@dataclass
class BumpTagUtils(TagUtils):
    def exist(self) -> bool:
        return self.config.patterns.increments.has_version_bump(self.value.lower())

    def get(self) -> VersionBump:
        return self.config.patterns.increments.parse_version_bump(self.value.lower())