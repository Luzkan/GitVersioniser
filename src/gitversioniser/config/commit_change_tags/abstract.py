import re
from abc import ABC

from gitversioniser.config.commit_change_tags.commit_tag import CommitTag
from gitversioniser.helpers.changelog_category import ChangelogCategory


class CommitChangeTags(ABC):
    def parse_line(self, message: str) -> tuple[ChangelogCategory, str]:
        """ The str in the tuple is the commit message, without the commit tag. """
        commit_tag: CommitTag
        for commit_tag in self.__dict__.values():
            if self.has_commit_tag(commit_tag, message):
                return (commit_tag.changelog_category, message[len(commit_tag.pattern) + message.find(commit_tag.pattern) + 1:])
        raise ValueError(f"Unknown Commit Tag in message: {message}")

    def has_any_commit_tag(self, commit_message_line: str) -> bool:
        return any([self.has_commit_tag(commit_tag, commit_message_line) for commit_tag in self.__dict__.values()])

    def has_commit_tag(self, commit_tag: CommitTag, commit_message_line: str) -> bool:
        return bool(re.match(f"^[^a-zA-Z]*{commit_tag.pattern}", commit_message_line))
