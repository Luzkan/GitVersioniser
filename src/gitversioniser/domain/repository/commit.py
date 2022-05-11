from dataclasses import dataclass, field

from git.objects import Commit as GitCommit

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.commit_utils.message import Message


@dataclass
class Commit:
    config: Config = field(repr=False)
    _commit: GitCommit = field(repr=False)

    def __post_init__(self):
        self.message = Message(self.config, str(self._commit.message))

    @property
    def get_parents_count(self) -> int:
        return int(self._commit.count())

    def get_parents(self) -> tuple['Commit', ...]:
        return tuple(Commit(self.config, _commit=parent) for parent in self._commit.parents)

    def is_made_by_author(self, author: str) -> bool:
        return author in [self._commit.committer.name, self._commit.author.name]
