from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ChangelogFile:
    path: Path
    lines: list[str]
    header_length: int = 0

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
        return self._recreate(lines=self._insert_lines_between_index(new_lines, self.line_index_for_new_entry))

    def add_footer(self, footer_line: str) -> 'ChangelogFile':
        return self._recreate(lines=[*self.lines, footer_line, '\n'])

    def save_file(self):
        with open(self.path, 'w') as changelog_file:
            changelog_file.writelines(self.lines)

    @staticmethod
    def init_from_path(changelog_path: Path) -> 'ChangelogFile':
        def load_changelog_lines():
            with open(changelog_path, "r") as changelog_file:
                return changelog_file.readlines()

        return ChangelogFile(
            path=changelog_path,
            lines=load_changelog_lines()
        )

    def _recreate(self, **kwargs: Path | list[str] | int) -> 'ChangelogFile':
        attributes = self.__dict__.copy() | kwargs
        return ChangelogFile(**attributes)

    def _insert_lines_between_index(self, new_lines: list[str], index: int):
        return [*self.lines[:index], *new_lines, '\n', *self.lines[index:]]
