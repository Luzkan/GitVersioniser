from gitversioniser.config.patterns.commit_change_tags.abstract import CommitMessageLine
from gitversioniser.domain.versioniser.routines.commit_message.describe_changes.abstract import DescribeChanges


class WithLetters(DescribeChanges):
    @staticmethod
    def run(list_of_changes: list[CommitMessageLine], description: str) -> str:
        if len(list_of_changes) <= 1:
            return description

        return f"{WithLetters.describe(list_of_changes)}{WithLetters.message_without_changes(list_of_changes, description)}"

    @staticmethod
    def describe(list_of_changes: list[CommitMessageLine]) -> str:
        return "\n".join([f"{commit_line.commit_tag.patterns} {commit_line.plain}" for commit_line in list_of_changes])

    @staticmethod
    def message_without_changes(list_of_changes: list[CommitMessageLine], message: str) -> str:
        for commit_line in list_of_changes:
            message = message.replace(commit_line.full, "")
        return message.replace('\n\n\n', '\n\n')
