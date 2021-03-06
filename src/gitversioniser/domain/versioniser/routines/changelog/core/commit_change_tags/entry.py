from dataclasses import dataclass, field
from typing import Generator


@dataclass
class ChangelogEntry:
    changes: dict[str, list[str]] = field(init=False, default_factory=dict)

    def create_category_entries(self) -> Generator[str, None, None]:
        for category, changes in self.changes.items():
            yield self._header(category) if changes else ""
            yield from changes
            yield "\n"

    def add(self, category: str, message: str):
        self.changes.setdefault(str(category), []).append(self._content(message))

    def add_custom(self, category: str, message: str):
        self.changes.setdefault(category, []).append(self._content(message))

    @staticmethod
    def _header(category_name: str) -> str:
        return f"### {category_name}\n\n"

    @staticmethod
    def _content(entry: str) -> str:
        return f"- {entry}\n"
