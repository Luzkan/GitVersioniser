from dataclasses import dataclass

from semver import VersionInfo

from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class PrefixVersionFull(RoutineCommitMessage):
    def run(self, new_version: VersionInfo) -> str:
        return f"[`{str(new_version)}`] {self.repo.commits.latest.summary}"

    @staticmethod
    def factory_name() -> str:
        return 'prefix_version_full'
