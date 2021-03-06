from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.commiting.abstract import RoutineCommiting
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass
class PushOriginNewCommit(RoutineCommiting):
    def run(self, result: VersioningResult):
        self.repo.remote.raise_if_changes()
        self.repo.files.add_all()
        self.repo.commits.commit(message=result.commit_message.new)
        self.repo.remote.push()
