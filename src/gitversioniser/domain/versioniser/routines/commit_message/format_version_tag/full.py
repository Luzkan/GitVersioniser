from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.commit_message.format_version_tag.abstract import FormatVersionTag


class Full(FormatVersionTag):
    @staticmethod
    def run(new_version: SemverTag) -> str:
        return str(new_version)
