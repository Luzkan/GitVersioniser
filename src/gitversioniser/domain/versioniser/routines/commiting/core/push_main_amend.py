from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersioningResult
from gitversioniser.domain.versioniser.routines.commiting.abstract import RoutineCommiting


@dataclass
class PushMainAmend(RoutineCommiting):
    def run(self, result: VersioningResult):
        self.repo.remote.raise_if_changes()
        self.repo.files.add_all()
        self.repo.commits.commit_amend(message=result.commit_message)
        self.repo.remote.push_force()

    @staticmethod
    def factory_name() -> str:
        return 'push_main_amend'
