from abc import ABC, abstractmethod

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.abstract import Routine
from gitversioniser.domain.versioniser.routines.commit_message.utils.commit_message_result import CommitMessageResult


class RoutineCommitMessage(Routine, ABC):
    def run(self, new_version: SemverTag) -> CommitMessageResult:
        return CommitMessageResult(
            old=self.repo.commits.latest.message.value,
            new=self.new_commit_message(new_version)
        )

    @abstractmethod
    def new_commit_message(self, new_version: SemverTag) -> str:
        pass
