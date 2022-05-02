from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class ChangelogFile:
    path: Path = field(repr=False)
    lines: list[str] = field(default_factory=list, repr=False)
    header_length: int = field(default=0, repr=False)
    entry_length: int = field(default=0, repr=False)

    @property
    def line_index_for_new_header(self):
        two_lines_after_horizontal_separator = 2
        return self.horizontal_line_index+two_lines_after_horizontal_separator

    @property
    def line_index_for_new_entry(self):
        return self.line_index_for_new_header+self.header_length

    @property
    def horizontal_line_index(self) -> int:
        for index, line in enumerate(self.lines):
            if line.rstrip() == '---':
                return index
        raise ValueError(f'No separator line found in {self.path}.')

    def add_header(self, new_lines: list[str]) -> 'ChangelogFile':
        return self._recreate(
            lines=self._insert_lines_between_index(new_lines, self.line_index_for_new_header),
            header_length=len(new_lines)
        )

    def add_entry(self, new_lines: list[str]) -> 'ChangelogFile':
        return self._recreate(
            lines=self._insert_lines_between_index(new_lines, self.line_index_for_new_entry),
            entry_length=len(new_lines)
        )

    def add_footer(self, footer_line: str) -> 'ChangelogFile':
        return self._recreate(lines=[*self.lines, footer_line])

    def save_file(self) -> 'ChangelogFile':
        with open(self.path, 'w', encoding='utf-8') as changelog_file:
            changelog_file.writelines(self.lines)
        return self

    @staticmethod
    def init_from_path(changelog_path: Path) -> 'ChangelogFile':
        def load_changelog_lines():
            with open(changelog_path, "r", encoding='utf-8') as changelog_file:
                return changelog_file.readlines()

        return ChangelogFile(
            path=changelog_path,
            lines=load_changelog_lines()
        )

    def _recreate(self, **kwargs: Path | list[str] | int) -> 'ChangelogFile':
        attributes: dict[str, Path | list[str] | int] = self.__dict__.copy() | kwargs
        return ChangelogFile(**attributes)  # type: ignore [arg-type]

    def _insert_lines_between_index(self, new_lines: list[str], index: int):
        return [*self.lines[:index], *new_lines, '\n', *self.lines[index:]]

    def __repr__(self) -> str:
        return ''.join([
            '\n',
            '-- -- -- -- --\n',
            *self.lines[self.line_index_for_new_header:self.line_index_for_new_header+self.entry_length+1],
            '-- -- -- -- --'
        ])
