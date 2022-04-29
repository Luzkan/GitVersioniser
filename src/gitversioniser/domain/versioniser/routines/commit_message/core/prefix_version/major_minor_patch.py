from dataclasses import dataclass

from semver import VersionInfo

from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class PrefixVersionMajorMinorPatch(RoutineCommitMessage):
    def run(self, new_version: VersionInfo) -> str:
        return f"[`{str(new_version.major)}.{str(new_version.minor)}.{str(new_version.patch)}`] " +\
               f"{self.target_repo.commits.latest.summary}"

    @staticmethod
    def factory_name() -> str:
        return 'prefix_version_major_minor_patch'
