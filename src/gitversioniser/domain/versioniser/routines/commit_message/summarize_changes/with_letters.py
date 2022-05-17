from gitversioniser.config.patterns.commit_change_tags.abstract import CommitMessageLine
from gitversioniser.domain.versioniser.routines.commit_message.summarize_changes.abstract import SummarizeChanges


class WithLetters(SummarizeChanges):
    @staticmethod
    def run(list_of_changes: list[CommitMessageLine], summary: str) -> str:
        if len(list_of_changes) < 1:
            return summary
        return f"{WithLetters.summarize(list_of_changes)}{WithLetters.remove_redundancies(list_of_changes, summary)}"

    @staticmethod
    def summarize(list_of_changes: list[CommitMessageLine]) -> str:
        return "/".join([commit_line.commit_tag.pattern.replace(":", '') for commit_line in list_of_changes]) + ': '

    @staticmethod
    def remove_redundancies(list_of_changes: list[CommitMessageLine], summary: str) -> str:
        for parsed_commit_line in list_of_changes:
            summary = summary.replace(parsed_commit_line.full, parsed_commit_line.plain)
        return summary
