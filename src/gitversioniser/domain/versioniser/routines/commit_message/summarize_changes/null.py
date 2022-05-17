from gitversioniser.config.patterns.commit_change_tags.abstract import CommitMessageLine
from gitversioniser.domain.versioniser.routines.commit_message.summarize_changes.abstract import SummarizeChanges


class Null(SummarizeChanges):
    @staticmethod
    def run(list_of_changes: list[CommitMessageLine], message: str) -> str:
        return message
