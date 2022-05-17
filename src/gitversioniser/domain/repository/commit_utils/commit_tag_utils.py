from dataclasses import dataclass

from gitversioniser.config.patterns.commit_change_tags.abstract import CommitMessageLine
from gitversioniser.domain.repository.commit_utils.tag import TagUtils


@dataclass
class CommitTagUtils(TagUtils):
    def exist(self) -> bool:
        return any([self.config.commit_patterns.change_tags.has_any_commit_tag(value) for value in self.value.split("\n")])

    def get(self) -> CommitMessageLine:
        """ returns: (ChangelogCategory, str: Commit Message without the Commit Tag) """
        return self.config.commit_patterns.change_tags.parse_line(self.value)

    def get_all(self) -> list[CommitMessageLine]:
        """ returns: (ChangelogCategory, str: Commit Message without the Commit Tag) """
        commit_tags = self.config.commit_patterns.change_tags
        return [commit_tags.parse_line(value) for value in self.value.split("\n") if commit_tags.has_any_commit_tag(value)]
