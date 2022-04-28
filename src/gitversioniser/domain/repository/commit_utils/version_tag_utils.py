from dataclasses import dataclass

from gitversioniser.domain.repository.commit_utils.tag import TagUtils
from gitversioniser.helpers.regex_pattern import RegexPattern


@dataclass
class VersionTagUtils(TagUtils):
    def exist(self) -> bool:
        return bool(RegexPattern.semver(self.value.lower()))
