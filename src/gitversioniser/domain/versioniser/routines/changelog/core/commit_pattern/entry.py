from dataclasses import dataclass, field
from typing import Generator

from gitversioniser.helpers.changelog_category import ChangelogCategory


@dataclass
class ChangelogEntry:
    changes: dict[str, list[str]] = field(init=False, default_factory=dict)

    def create_category_entries(self) -> Generator[str, None, None]:
        for category, changes in self.changes.items():
            yield self.header(category) if changes else ""
            yield from changes
            yield "\n"

    def add(self, category: ChangelogCategory, message: str):
        self.changes.setdefault(str(category.value), []).append(self.content(message))

    def add_custom(self, category: str, message: str):
        self.changes.setdefault(category, []).append(self.content(message))

    def header(self, category_name: str) -> str:
        return f"### {category_name}\n\n"

    def content(self, entry: str) -> str:
        return f"- {entry}\n"
