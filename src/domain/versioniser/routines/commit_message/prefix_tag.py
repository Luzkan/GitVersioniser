from dataclasses import dataclass

from semver import VersionInfo

from domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class PrefixTag(RoutineCommitMessage):
    """
    Adds the new version to the commit message as a prefix.

    Examples:
        [`1.0.1`] Added Foo to Goo
        [`1.4.3+build.2`] Tweaked the main div margin
    """

    def run(self, new_version: VersionInfo) -> str:
        return f"[`{str(new_version)}`] {self.target_repo.commits.latest.summary}"

    @staticmethod
    def factory_name() -> str:
        return 'prefix_tag'
