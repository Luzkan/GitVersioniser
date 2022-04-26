from dataclasses import dataclass, field

from config.config import Config
from domain.repository.git_repository import GitRepository
from domain.versioniser.helpers.routine_result import VersionisingResult
from domain.versioniser.routines.changelog.abstract import RoutineChangelog
from domain.versioniser.routines.changelog.factory import RoutineChangelogFactory
from domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage
from domain.versioniser.routines.commit_message.factory import RoutineCommitFactory
from domain.versioniser.routines.contribution.abstract import RoutineContribution
from domain.versioniser.routines.contribution.factory import RoutineContributionFactory
from domain.versioniser.routines.file_updater.abstract import RoutineFileUpdater
from domain.versioniser.routines.file_updater.factory import RoutineFileUpdaterFactory
from domain.versioniser.routines.version.abstract import RoutineVersion
from domain.versioniser.routines.version.factory import RoutineVersionFactory


@dataclass
class RoutineManager:
    config: Config
    target_repo: GitRepository
    version: RoutineVersion = field(init=False)
    commit_message: RoutineCommitMessage = field(init=False)
    contribution: RoutineContribution = field(init=False)
    file_updater: RoutineFileUpdater = field(init=False)
    changelog: RoutineChangelog = field(init=False)

    def __post_init__(self):
        def init_submodules():
            self.version = RoutineVersionFactory.create(self.config.routines.version)(self.config, self.target_repo)
            self.commit_message = RoutineCommitFactory.create(self.config.routines.commit_message)(self.config, self.target_repo)
            self.contribution = RoutineContributionFactory.create(self.config.routines.contribution)(self.config, self.target_repo)
            self.file_updater = RoutineFileUpdaterFactory.create(self.config.routines.file_updater)(self.config, self.target_repo)
            self.changelog = RoutineChangelogFactory.create(self.config.routines.changelog)(self.config, self.target_repo)

        init_submodules()

    def perform_versionising(self) -> VersionisingResult:
        versions = self.version.run()
        self.file_updater.run(versions)
        self.changelog.run(versions.new)
        return VersionisingResult(
            versions=versions,
            commit_message=self.commit_message.run(versions.new)
        )

    def run(self):
        result: VersionisingResult = self.perform_versionising()
        self.contribution.run(result)
