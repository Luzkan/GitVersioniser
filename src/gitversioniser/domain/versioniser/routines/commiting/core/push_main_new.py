from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersionisingResult
from gitversioniser.domain.versioniser.routines.commiting.abstract import RoutineCommiting


@dataclass
class PushMainNew(RoutineCommiting):
    def run(self, result: VersionisingResult):
        self.target_repo.remote.raise_if_changes()
        self.target_repo.files.add_all()
        self.target_repo.commits.commit(message=result.commit_message)
        self.target_repo.remote.push()

    @staticmethod
    def factory_name() -> str:
        return 'push_main_new'
