from gitversioniser.config.patterns.commit_change_tags.abstract import CommitMessageLine
from gitversioniser.domain.versioniser.routines.commit_message.describe_changes.abstract import DescribeChanges


class Null(DescribeChanges):
    @staticmethod
    def run(list_of_changes: list[CommitMessageLine], description: str) -> str:
        return ""
