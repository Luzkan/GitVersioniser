from dataclasses import dataclass

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class SuffixVersionMajorMinorPatch(RoutineCommitMessage):
    def new_commit_message(self, new_version: SemverTag) -> str:
        return f"{self.repo.commits.latest.message.value.rstrip()} " +\
               f"[`{new_version.to_string(with_prerelease=False, with_build=False)}`]"
