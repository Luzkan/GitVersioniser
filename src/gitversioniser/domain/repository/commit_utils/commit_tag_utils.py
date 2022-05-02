from dataclasses import dataclass

from gitversioniser.domain.repository.commit_utils.tag import TagUtils
from gitversioniser.helpers.changelog_category import ChangelogCategory


@dataclass
class CommitTagUtils(TagUtils):
    def exist(self) -> bool:
        return any([self.config.patterns.commit_tags.has_commit_tag(value) for value in self.value.split("\n")])

    def get(self) -> tuple[ChangelogCategory, str]:
        """ The str in the tuple is the commit message, without the commit tag. """
        return self.config.patterns.commit_tags.parse_line(self.value)

    def get_all(self) -> list[tuple[ChangelogCategory, str]]:
        """ The str in the tuple is the commit message, without the commit tag. """
        commit_tags = self.config.patterns.commit_tags
        return [commit_tags.parse_line(value) for value in self.value.split("\n") if commit_tags.has_commit_tag(value)]
