
from dataclasses import dataclass, field

from typing_extensions import Self

from gitversioniser.config.patterns.commit_change_tags.abstract import CommitMessageLine
from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.commit_message.describe_changes.abstract import DescribeChanges
from gitversioniser.domain.versioniser.routines.commit_message.format_version_tag.abstract import FormatVersionTag
from gitversioniser.domain.versioniser.routines.commit_message.place_version_tag.abstract import PlaceVersionTag
from gitversioniser.domain.versioniser.routines.commit_message.summarize_changes.abstract import SummarizeChanges


@dataclass(frozen=True)
class NewCommitMessage:
    new_version: SemverTag = field(repr=False)
    list_of_changes: list[CommitMessageLine] = field(repr=False)
    summary: str
    description: str
    footer: str

    def __str__(self) -> str:
        return '\n\n'.join([part for part in [self.summary.rstrip(), self.description.rstrip(), self.footer.rstrip()] if part])

    def add_version_tag_to_summary(self, placement: PlaceVersionTag, formatter: FormatVersionTag) -> Self:
        return self._recreate(summary=placement.run(formatter.run(self.new_version), self.summary))

    def add_summarized_changes_to_summary(self, summarizer: SummarizeChanges) -> Self:
        return self._recreate(summary=summarizer.run(self.list_of_changes, self.summary))

    def describe_changes_in_description(self, describe_changes: DescribeChanges) -> Self:
        return self._recreate(description=describe_changes.run(self.list_of_changes, self.description))

    def remove_footer_redundancies(self):
        footer: str = self.footer
        for parsed_commit_line in self.list_of_changes:
            footer = footer.replace(parsed_commit_line.full, '')
        return self._recreate(footer=footer)

    def _recreate(self, **kwargs: str) -> 'NewCommitMessage':
        attributes: dict = self.__dict__.copy() | kwargs
        return NewCommitMessage(**attributes)  # type: ignore [arg-type]
