from dataclasses import dataclass, field

from git import Commit as GitCommit

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.commit_utils.message import Message
from gitversioniser.domain.repository.commit_utils.summary import Summary


@dataclass
class Commit:
    """ Couldn't make it with inheritance. """
    config: Config
    _commit: GitCommit
    message: Message = field(init=False)

    @property
    def summary(self) -> Summary:
        """ Summary is just a part of message, but it's handy to use it as a property. """
        return self.message.summary

    def __post_init__(self):
        self.message = Message(self.config, str(self._commit.message))

    @property
    def get_parents_count(self) -> int:
        return self._commit.count()

    def get_parent(self) -> 'Commit':
        return Commit(self.config, _commit=self._commit.parents[0])

    def is_made_by_author(self, author: str) -> bool:
        return self._commit.committer.name == author or self._commit.author.name == author
