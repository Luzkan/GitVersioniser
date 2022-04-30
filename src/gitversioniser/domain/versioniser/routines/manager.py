from dataclasses import dataclass

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.git_repository import GitRepository
from gitversioniser.domain.versioniser.helpers.routine_result import VersionisingResult
from gitversioniser.domain.versioniser.routines.changelog import RoutineChangelog, RoutineChangelogFactory
from gitversioniser.domain.versioniser.routines.commit_message import RoutineCommitMessage, RoutineCommitMessageFactory
from gitversioniser.domain.versioniser.routines.commiting import RoutineCommiting, RoutineCommitingFactory
from gitversioniser.domain.versioniser.routines.file_updater import RoutineFileUpdater, RoutineFileUpdaterFactory
from gitversioniser.domain.versioniser.routines.tagging import RoutineTagging, RoutineTaggingFactory
from gitversioniser.domain.versioniser.routines.version import RoutineVersion, RoutineVersionFactory


@dataclass
class RoutineManager:
    config: Config
    target_repo: GitRepository

    def __post_init__(self):
        deps: tuple[Config, GitRepository] = (self.config, self.target_repo)
        self.version: RoutineVersion = RoutineVersionFactory.create(self.config.routines.version)(*deps)
        self.commit_message: RoutineCommitMessage = RoutineCommitMessageFactory.create(self.config.routines.commit_message)(*deps)
        self.commiting: RoutineCommiting = RoutineCommitingFactory.create(self.config.routines.commiting)(*deps)
        self.file_updater: RoutineFileUpdater = RoutineFileUpdaterFactory.create(self.config.routines.file_updater)(*deps)
        self.changelog: RoutineChangelog = RoutineChangelogFactory.create(self.config.routines.changelog)(*deps)
        self.tagging: RoutineTagging = RoutineTaggingFactory.create(self.config.routines.tagging)(*deps)

    def versionise(self) -> VersionisingResult:
        versions = self.version.run()
        return VersionisingResult(
            versions=versions,
            commit_message=self.commit_message.run(versions.new)
        )

    def contribute(self, result: VersionisingResult):
        self.commiting.run(result)
        self.tagging.run(result)

    def run(self):
        result: VersionisingResult = self.versionise()
        self.contribute(result)
