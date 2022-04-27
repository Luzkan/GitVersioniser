from dataclasses import dataclass

from gitversioniser.config.commit_tag import CommitTag
from gitversioniser.helpers.changelog_category import ChangelogCategory


@dataclass
class CommitTags:
    added: CommitTag = CommitTag("A:", ChangelogCategory.ADDED)
    changed: CommitTag = CommitTag("C:", ChangelogCategory.CHANGED)
    deprecated: CommitTag = CommitTag("D:", ChangelogCategory.DEPRECATED)
    removed: CommitTag = CommitTag("R:", ChangelogCategory.REMOVED)
    fixed: CommitTag = CommitTag("F:", ChangelogCategory.FIXED)
    security: CommitTag = CommitTag("S:", ChangelogCategory.SECURITY)

    def get_default_dict_for_changelog(self) -> dict[str, list[str]]:
        return {str(commit_tag.changelog_category.value): list() for commit_tag in self.__dict__.values()}

    def parse_commit(self, commit_message: str) -> tuple[ChangelogCategory, str]:
        """ The str in the tuple is the commit message, without the commit tag. """
        commit_tag: CommitTag
        for commit_tag in self.__dict__.values():
            if str(commit_tag.pattern) in commit_message:
                return (commit_tag.changelog_category, commit_message.replace(f"{str(commit_tag.pattern)} ", ""))
        raise ValueError(f"Unknown Commit Tag in message: {commit_message}")

    def has_commit_tag(self, commit_message: str) -> bool:
        return any([commit_message.startswith(commit_tag.pattern) for commit_tag in self.__dict__.values()])
