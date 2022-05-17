from dataclasses import dataclass

from gitversioniser.config.routines.commit_message import CommitMessageArguments
from gitversioniser.domain.versioniser.routines.commit_message import (
    DescribeChangesFactory,
    FormatVersionTagFactory,
    PlaceVersionTagFactory,
    RoutineCommitMessage,
    SummarizeChangesFactory,
)


@dataclass
class RoutineCommitMessageFactory:
    commit_message_arguments: CommitMessageArguments

    def create(self, dependencies) -> RoutineCommitMessage:
        return RoutineCommitMessage(
            *dependencies,
            describe_changes=DescribeChangesFactory.create(self.commit_message_arguments.describe_changes)(*dependencies),
            format_version_tag=FormatVersionTagFactory.create(self.commit_message_arguments.format_version_tag)(*dependencies),
            place_version_tag=PlaceVersionTagFactory.create(self.commit_message_arguments.place_version_tag)(*dependencies),
            summarize_changes=SummarizeChangesFactory.create(self.commit_message_arguments.summarize_changes)(*dependencies),
        )
