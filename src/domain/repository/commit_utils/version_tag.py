from dataclasses import dataclass

from domain.repository.commit_utils.tag import TagUtils
from helpers.regex.pattern_semver import regex_pattern_semver


@dataclass
class VersionTagUtils(TagUtils):
    def exist(self) -> bool:
        return bool(regex_pattern_semver(self.value.lower()))
