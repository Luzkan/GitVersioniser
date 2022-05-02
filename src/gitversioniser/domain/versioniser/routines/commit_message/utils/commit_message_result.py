from dataclasses import dataclass


@dataclass(frozen=True)
class CommitMessageResult:
    old: str
    new: str
