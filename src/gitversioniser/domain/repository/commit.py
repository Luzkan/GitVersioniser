from dataclasses import dataclass, field

from git.objects import Commit as GitCommit

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.commit_utils.message import Message
from gitversioniser.domain.repository.commit_utils.summary import Summary


@dataclass
class Commit:
    """ Couldn't make it with inheritance. """
    config: Config = field(repr=False)
    _commit: GitCommit = field(repr=False)
    message: Message = field(init=False)

    @property
    def summary(self) -> Summary:
        """ Summary is just a part of message, but it's handy to use it as a property. """
        return self.message.summary

    @property
    def description(self) -> str:
        return self.message.value.replace(str(self.message.summary), '')

    def __post_init__(self):
        self.message = Message(self.config, str(self._commit.message))

    @property
    def get_parents_count(self) -> int:
        return int(self._commit.count())

    def get_parents(self) -> tuple['Commit', ...]:
        return tuple(Commit(self.config, _commit=parent) for parent in self._commit.parents)

    def is_made_by_author(self, author: str) -> bool:
        return author in [self._commit.committer.name, self._commit.author.name]
