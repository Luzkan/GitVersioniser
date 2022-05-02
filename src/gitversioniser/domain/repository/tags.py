from dataclasses import dataclass

from git import TagReference
from git.repo import Repo
from semver import VersionInfo

from gitversioniser.helpers.regex_pattern import RegexPattern


@dataclass
class Tags:
    repo: Repo

    def create(self, tag: str):
        return self.repo.create_tag(tag)

    @property
    def get(self) -> list[TagReference]:
        return self.repo.tags

    @property
    def get_semvers_sorted(self) -> list[str]:
        return sorted([
            self._truncate_v_from_semver(str(tag)) for tag in self.repo.git.tag("-l", "--sort=-v:refname", "*.*.*").split('\n')
        ], reverse=True)

    @property
    def get_sorted(self) -> list[str]:
        return [str(tag) for tag in self.repo.git.tag("--sort=-v:refname").split('\n')]

    @staticmethod
    def _truncate_v_from_semver(tag_semver: str) -> str:
        return tag_semver[1:] if tag_semver and tag_semver[0] == 'v' else tag_semver

    @property
    def latest_semver(self) -> VersionInfo:
        for tag in self.get_semvers_sorted:
            if RegexPattern.semver(tag):
                return VersionInfo.parse(tag)
        return VersionInfo(0, 0, 0)
