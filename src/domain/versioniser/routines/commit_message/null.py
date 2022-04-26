from dataclasses import dataclass

from semver import VersionInfo

from domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class Null(RoutineCommitMessage):
    """
    Does not change the original commit message.
    """

    def run(self, new_version: VersionInfo) -> str:
        return str(self.target_repo.commits.latest.summary)

    @staticmethod
    def factory_name() -> str:
        return 'null'
