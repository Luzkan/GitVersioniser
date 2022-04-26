from dataclasses import dataclass

from domain.versioniser.helpers.routine_result import VersionisingResult
from domain.versioniser.routines.contribution.abstract import RoutineContribution


@dataclass
class PushMainAmend(RoutineContribution):
    """
    Adds the version by amending to the latest commit on main branch.
    Works best with:
        - Solo Projects
    """

    def run(self, result: VersionisingResult):
        self.target_repo.remote.raise_if_changes()
        self.target_repo.files.add_all()
        self.target_repo.commits.commit_amend(message=result.commit_message)
        self.target_repo.remote.push_force()
        self.target_repo.remote.create_tag(version=str(result.versions.new))
        self.target_repo.remote.push_tags()

    @staticmethod
    def factory_name() -> str:
        return 'push_main_amend'
