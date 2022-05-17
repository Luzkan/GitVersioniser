
from dataclasses import dataclass

from gitversioniser.helpers.types import (
    ROUTINE_COMMIT_MESSAGE_DESCRIBE_CHANGES,
    ROUTINE_COMMIT_MESSAGE_FORMAT_VERSION_TAG,
    ROUTINE_COMMIT_MESSAGE_PLACE_VERSION_TAG,
    ROUTINE_COMMIT_MESSAGE_SUMMARIZE_CHANGES,
)


@dataclass(frozen=True)
class CommitMessageArguments:
    describe_changes: ROUTINE_COMMIT_MESSAGE_DESCRIBE_CHANGES
    format_version_tag: ROUTINE_COMMIT_MESSAGE_FORMAT_VERSION_TAG
    place_version_tag: ROUTINE_COMMIT_MESSAGE_PLACE_VERSION_TAG
    summarize_changes: ROUTINE_COMMIT_MESSAGE_SUMMARIZE_CHANGES
