from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.commit_message.utils.new_commit_message import NewCommitMessage


@dataclass(frozen=True)
class CommitMessageResult:
    old: str
    new: NewCommitMessage
