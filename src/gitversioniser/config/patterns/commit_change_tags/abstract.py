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
            for pattern in commit_tag.patterns:
                if self.has_commit_tag(pattern, message):
                    return CommitMessageLine(
                        commit_tag=commit_tag,
                        plain=message[len(pattern) + message.find(pattern) + 1:],
                        full=message
                    )
        raise ValueError(f"Unknown Commit Tag in message: {message}")

    def has_any_commit_tag(self, commit_message_line: str) -> bool:
        return any([
            self.has_commit_tag(pattern, commit_message_line)
            for commit_tag in self.__dict__.values()
            for pattern in commit_tag.patterns
        ])

    def has_commit_tag(self, pattern: str, commit_message_line: str) -> bool:
        return bool(re.match(f"^[^a-zA-Z]*{pattern}", commit_message_line))
