from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.versions import Versions
from gitversioniser.helpers.regex_pattern import RegexPattern


@dataclass
class VersionComparer:
    versions: Versions

    def is_new_major(self) -> bool:
        return self.versions.new.major > self.versions.old.major

    def is_new_minor(self) -> bool:
        return (self.versions.new.major == self.versions.old.major) and\
               (self.versions.new.minor > self.versions.old.minor)

    def is_new_patch(self) -> bool:
        return (self.versions.new.major == self.versions.old.major) and\
               (self.versions.new.minor == self.versions.old.minor) and\
               (self.versions.new.patch > self.versions.old.patch)

    def is_new_prerelease(self) -> bool:
        return (self.versions.new.major == self.versions.old.major) and\
               (self.versions.new.minor == self.versions.old.minor) and\
               (self.versions.new.patch == self.versions.old.patch) and\
               (self.semver_substring_to_number(self.versions.new.prerelease) > self.semver_substring_to_number(self.versions.old.prerelease))

    def is_new_build(self) -> bool:
        return (self.versions.new.major == self.versions.old.major) and\
               (self.versions.new.minor == self.versions.old.minor) and\
               (self.versions.new.patch == self.versions.old.patch) and\
               (self.semver_substring_to_number(self.versions.new.prerelease) == self.semver_substring_to_number(self.versions.old.prerelease)) and\
               (self.semver_substring_to_number(self.versions.new.prerelease) > self.semver_substring_to_number(self.versions.old.prerelease))

    def semver_substring_to_number(self, semver_substring: str | None) -> int:
        if not semver_substring:
            return 0
        match = RegexPattern.semver_substring_to_number(semver_substring)
        return int(match.group(1)) if match else 0
