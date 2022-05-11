from dataclasses import dataclass
from typing import Optional

from gitversioniser.helpers.changelog_category import ChangelogCategory


@dataclass(frozen=True)
class CommitTag:
    pattern: str
    changelog_category: ChangelogCategory
    emoji_representation: Optional[str] = None

    def __str__(self):
        return self.pattern
