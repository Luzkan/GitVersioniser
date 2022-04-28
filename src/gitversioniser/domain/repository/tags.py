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
    def get_sorted(self) -> list[str]:
        return [str(tag) for tag in self.repo.git.tag("--sort=-v:refname").split('\n')]

    @property
    def latest_semver(self) -> VersionInfo:
        def truncate_v_from_semver(tag_semver: str) -> str:
            return tag_semver[1:] if tag_semver and tag_semver[1] == 'v' else tag_semver

        for tag in self.get_sorted:
            if RegexPattern.semver(truncate_v_from_semver(tag)):
                return VersionInfo.parse(tag)
        return VersionInfo(0, 0, 0)
