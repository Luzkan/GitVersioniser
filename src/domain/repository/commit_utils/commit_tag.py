from dataclasses import dataclass

from domain.repository.commit_utils.tag import TagUtils
from helpers.changelog_category import ChangelogCategory


@dataclass
class CommitTagUtils(TagUtils):
    def exist(self) -> bool:
        return self.config.patterns.commit_tags.has_commit_tag(self.value)

    def get(self) -> tuple[ChangelogCategory, str]:
        """ The str in the tuple is the commit message, without the commit tag. """
        return self.config.patterns.commit_tags.parse_commit(self.value)
