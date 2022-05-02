from dataclasses import dataclass

from git import TagReference
from git.repo import Repo

from gitversioniser.domain.repository.semver_tag import SemverTag


@dataclass
class Tags:
    repo: Repo

    def create(self, tag: str):
        return self.repo.create_tag(tag)

    @property
    def get(self) -> list[TagReference]:
        return self.repo.tags

    @property
    def get_sorted_semvers(self) -> list[SemverTag]:
        return sorted([
            SemverTag.init(str(tag)) for tag in self.repo.git.tag("-l", "--sort=-v:refname", "*.*.*").split('\n') if SemverTag.is_valid(str(tag))
        ], reverse=True)

    @property
    def get_sorted(self) -> list[str]:
        return [str(tag) for tag in self.repo.git.tag("--sort=-v:refname").split('\n')]

    @property
    def latest_semver(self) -> SemverTag:
        return self.get_sorted_semvers[0] if self.get_sorted_semvers else SemverTag.init('0.0.0')
