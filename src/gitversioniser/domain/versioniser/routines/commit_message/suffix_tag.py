from dataclasses import dataclass

from semver import VersionInfo

from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class SuffixTag(RoutineCommitMessage):
    """
    Adds the new version to the commit message as a prefix.

    Examples:
        Added Foo to Goo [`1.0.1`]
        Tweaked the main div margin [`1.4.3+build.2`]
    """

    def run(self, new_version: VersionInfo) -> str:
        return f"{self.target_repo.commits.latest.summary} [`{str(new_version)}`]"

    @staticmethod
    def factory_name() -> str:
        return 'suffix_tag'
