from dataclasses import dataclass

from gitversioniser.domain.versioniser.helpers.routine_result import VersionisingResult
from gitversioniser.domain.versioniser.routines.contribution.abstract import RoutineContribution


@dataclass
class PushMainNew(RoutineContribution):
    """
    Adds the version in a new commit.
    Works best with:
        - Solo & Team Projects
    """

    def run(self, result: VersionisingResult):
        self.target_repo.files.add_all()
        self.target_repo.commits.commit(message=result.commit_message)
        self.target_repo.remote.push()
        self.target_repo.remote.create_tag(version=str(result.versions.new))
        self.target_repo.remote.push_tags()

    @staticmethod
    def factory_name() -> str:
        return 'push_main_new'
