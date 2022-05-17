import re
from abc import ABC
from dataclasses import dataclass

from gitversioniser.config.patterns.commit_change_tags.commit_tag import CommitTag


@dataclass(frozen=True)
class CommitMessageLine:
    commit_tag: CommitTag
    plain: str
    full: str


class CommitChangeTags(ABC):
    def parse_line(self, message: str) -> CommitMessageLine:
        """ The str in the tuple is the commit message, without the commit tag. """
        commit_tag: CommitTag
        for commit_tag in self.__dict__.values():
            if self.has_commit_tag(commit_tag, message):
                return CommitMessageLine(
                    commit_tag=commit_tag,
                    plain=message[len(commit_tag.pattern) + message.find(commit_tag.pattern) + 1:],
                    full=message
                )
        raise ValueError(f"Unknown Commit Tag in message: {message}")

    def has_any_commit_tag(self, commit_message_line: str) -> bool:
        return any([self.has_commit_tag(commit_tag, commit_message_line) for commit_tag in self.__dict__.values()])

    def has_commit_tag(self, commit_tag: CommitTag, commit_message_line: str) -> bool:
        return bool(re.match(f"^[^a-zA-Z]*{commit_tag.pattern}", commit_message_line))
