from collections import Counter

from gitversioniser.config.patterns.commit_change_tags.abstract import CommitMessageLine
from gitversioniser.domain.versioniser.routines.commit_message.summarize_changes.abstract import SummarizeChanges


class WithEmojiCounted(SummarizeChanges):
    @staticmethod
    def run(list_of_changes: list[CommitMessageLine], summary: str) -> str:
        if len(list_of_changes) < 1:
            return summary

        return f"{WithEmojiCounted.summarize(list_of_changes)}{WithEmojiCounted.remove_redundancies(list_of_changes, summary)}"

    @staticmethod
    def summarize(list_of_changes: list[CommitMessageLine]) -> str:
        return "".join([
            f"{tag}{WithEmojiCounted.convert_to_power_unicode(count)}" for tag, count in WithEmojiCounted.count_changes(list_of_changes).items()
        ]) + ' '

    @staticmethod
    def count_changes(list_of_changes: list[CommitMessageLine]) -> dict[str, int]:
        return Counter([commit_line.commit_tag.emoji_representation for commit_line in list_of_changes])

    @staticmethod
    def convert_to_power_unicode(number: int) -> str:
        MAPPING = {
            '1': '¹',
            '2': '²',
            '3': '³',
            '4': '⁴',
            '5': '⁵',
            '6': '⁶',
            '7': '⁷',
            '8': '⁸',
            '9': '⁹',
            '0': '⁰'
        }
        return ''.join([MAPPING[numeric_character] for numeric_character in str(number)]) if number > 1 else ''

    @staticmethod
    def remove_redundancies(list_of_changes: list[CommitMessageLine], summary: str) -> str:
        for parsed_commit_line in list_of_changes:
            summary = summary.replace(parsed_commit_line.full, parsed_commit_line.plain)
        return summary
