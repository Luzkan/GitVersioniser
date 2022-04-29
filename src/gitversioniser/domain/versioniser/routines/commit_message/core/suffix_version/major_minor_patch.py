from dataclasses import dataclass

from semver import VersionInfo

from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class SuffixVersionMajorMinorPatch(RoutineCommitMessage):
    def run(self, new_version: VersionInfo) -> str:
        return f"{self.target_repo.commits.latest.summary} " +\
               f"[`{str(new_version.major)}.{str(new_version.minor)}.{str(new_version.patch)}`]"

    @staticmethod
    def factory_name() -> str:
        return 'suffix_version_major_minor_patch'
