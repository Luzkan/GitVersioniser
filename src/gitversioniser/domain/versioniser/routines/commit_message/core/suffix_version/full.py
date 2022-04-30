from dataclasses import dataclass

from semver import VersionInfo

from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class SuffixVersionFull(RoutineCommitMessage):
    def run(self, new_version: VersionInfo) -> str:
        return f"{self.repo.commits.latest.summary} [`{str(new_version)}`]"

    @staticmethod
    def factory_name() -> str:
        return 'suffix_version'
