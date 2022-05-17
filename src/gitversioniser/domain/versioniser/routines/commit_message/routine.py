from dataclasses import dataclass

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.domain.versioniser.routines.commit_message.describe_changes.abstract import DescribeChanges
from gitversioniser.domain.versioniser.routines.commit_message.format_version_tag.abstract import FormatVersionTag
from gitversioniser.domain.versioniser.routines.commit_message.place_version_tag.abstract import PlaceVersionTag
from gitversioniser.domain.versioniser.routines.commit_message.summarize_changes.abstract import SummarizeChanges
from gitversioniser.domain.versioniser.routines.commit_message.utils.commit_message_result import CommitMessageResult
from gitversioniser.domain.versioniser.routines.commit_message.utils.new_commit_message import NewCommitMessage


@dataclass
class RoutineCommitMessage(Routine):
    place_version_tag: PlaceVersionTag
    format_version_tag: FormatVersionTag
    summarize_changes: SummarizeChanges
    describe_changes: DescribeChanges

    def run(self, new_version: SemverTag) -> CommitMessageResult:
        return CommitMessageResult(
            old=self.repo.commits.latest.message.value,
            new=NewCommitMessage(
                new_version=new_version,
                list_of_changes=self.repo.commits.latest.message.commit_tag.get_all(),
                summary=self.repo.commits.latest.message.summary,
                description=self.repo.commits.latest.message.description,
                footer=self.repo.commits.latest.message.footer
            )
            .remove_footer_redundancies()
            .add_summarized_changes_to_summary(self.summarize_changes)
            .add_version_tag_to_summary(self.place_version_tag, self.format_version_tag)
            .describe_changes_in_description(self.describe_changes)
        )
