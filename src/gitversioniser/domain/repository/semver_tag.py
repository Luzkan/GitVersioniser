from dataclasses import dataclass
from typing import Optional

from semver import VersionInfo

from gitversioniser.helpers.regex_pattern import RegexPattern


@dataclass(frozen=True)
class SemverTag:
    _semver: VersionInfo

    @staticmethod
    def init(string: str) -> 'SemverTag':
        if not SemverTag.is_valid(string):
            raise ValueError(f'{string} is not a valid semver tag')
        return SemverTag(VersionInfo.parse(SemverTag.truncate_v_from_semver(string)))

    @classmethod
    def is_valid(cls, string: str) -> bool:
        return bool(RegexPattern.semver(SemverTag.truncate_v_from_semver(string)))

    @staticmethod
    def init_spec(
        major: int,
        minor: Optional[int] = 0,
        patch: Optional[int] = 0,
        prerelease: Optional[str] = None,
        build: Optional[str] = None
    ) -> 'SemverTag':
        """ Deprecate it asap """
        return SemverTag(VersionInfo(major, minor, patch, prerelease=prerelease, build=build))

    @property
    def major(self) -> str:
        return str(self._semver.major)

    @property
    def minor(self) -> str:
        return str(self._semver.minor)

    @property
    def patch(self) -> str:
        return str(self._semver.patch)

    @property
    def prerelease(self) -> str | None:
        return self._semver.prerelease

    @property
    def build(self) -> str | None:
        return self._semver.build

    def bump_major(self) -> 'SemverTag':
        return SemverTag(self._semver.bump_major())

    def bump_minor(self) -> 'SemverTag':
        return SemverTag(self._semver.bump_minor())

    def bump_patch(self) -> 'SemverTag':
        return SemverTag(self._semver.bump_patch())

    def bump_prerelease(self, default_name: str = "rc") -> 'SemverTag':
        return SemverTag(self._semver.bump_prerelease(default_name))

    def bump_build(self) -> 'SemverTag':
        return SemverTag(self._semver.bump_build())

    def finalize_version(self) -> 'SemverTag':
        return SemverTag(self._semver.finalize_version())

    def to_acronym(self, with_prerelease=True, with_build=True) -> str:
        version_tag: str = f"{self.major}.{self.minor}.{self.patch}"
        version_tag += f"-{self._filter_to_digit(self.prerelease)}" if self.prerelease and with_prerelease else ""
        version_tag += f"+{self._filter_to_digit(self.build)}" if self.build and with_build else ""
        return version_tag

    def to_string(self, with_prerelease=True, with_build=True) -> str:
        version_tag: str = f"{self.major}.{self.minor}.{self.patch}"
        version_tag += f"-{self.prerelease}" if self.prerelease and with_prerelease else ""
        version_tag += f"+{self.build}" if self.build and with_build else ""
        return version_tag

    def to_tuple(self) -> tuple[int, int, int, int, int]:
        return (
            self._filter_to_digit(self.major),
            self._filter_to_digit(self.minor),
            self._filter_to_digit(self.patch),
            self._filter_to_digit(self.prerelease) + self._evaluate_common_prerelease_name(self.prerelease),
            self._filter_to_digit(self.build)
        )

    def __str__(self) -> str:
        return str(self._semver)

    @staticmethod
    def _evaluate_common_prerelease_name(prerelease_name: str | None) -> int:
        SCORES_TABLE: dict[str | None, int] = {
            "alpha": 1000,
            "beta": 2000,
            "rc": 3000,
            None: 10000,
        }
        return SCORES_TABLE[next((key for key in SCORES_TABLE if str(key) in str(prerelease_name)), None)]

    @staticmethod
    def _filter_to_digit(version: str | None) -> int:
        digits = "".join(filter(str.isdigit, str(version)))
        return int(digits) if digits else 0

    def __lt__(self, other: 'SemverTag'):
        return self.to_tuple() < other.to_tuple()

    @staticmethod
    def truncate_v_from_semver(tag_semver: str) -> str:
        return tag_semver[1:] if tag_semver and tag_semver[0] == 'v' else tag_semver
