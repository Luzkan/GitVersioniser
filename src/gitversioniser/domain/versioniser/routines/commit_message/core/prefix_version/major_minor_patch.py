from dataclasses import dataclass

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class PrefixVersionMajorMinorPatch(RoutineCommitMessage):
    def new_commit_message(self, new_version: SemverTag) -> str:
        return f"[`{new_version.to_string(with_prerelease=False, with_build=False)}`] " +\
               f"{self.repo.commits.latest.message.value.rstrip()}"

    @staticmethod
    def factory_name() -> str:
        return 'prefix_version_major_minor_patch'
