from dataclasses import dataclass

from gitversioniser.helpers.changelog_category import ChangelogCategory


@dataclass
class CommitTag:
    pattern: str
    changelog_category: ChangelogCategory

    def __str__(self):
        return self.pattern
