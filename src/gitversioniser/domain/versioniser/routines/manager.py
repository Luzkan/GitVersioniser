from dataclasses import dataclass

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.git_repository import GitRepository
from gitversioniser.domain.versioniser.routines.changelog import RoutineChangelog, RoutineChangelogFactory
from gitversioniser.domain.versioniser.routines.commit_message import RoutineCommitMessage, RoutineCommitMessageFactory
from gitversioniser.domain.versioniser.routines.commiting import RoutineCommiting, RoutineCommitingFactory
from gitversioniser.domain.versioniser.routines.file_updater import RoutineFileUpdater, RoutineFileUpdaterFactory
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.abstract import RoutinePrefixTagWithV
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v.factory import RoutinePrefixTagWithVFactory
from gitversioniser.domain.versioniser.routines.should_contribute import RoutineShouldContribute, RoutineShouldContributeFactory
from gitversioniser.domain.versioniser.routines.tagging import RoutineTagging, RoutineTaggingFactory
from gitversioniser.domain.versioniser.routines.version import RoutineVersion, RoutineVersionFactory
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass
class RoutineManager:
    config: Config
    repository: GitRepository

    def __post_init__(self):
        deps: tuple[Config, GitRepository] = (self.config, self.repository)
        self.tagging: RoutineTagging = RoutineTaggingFactory.create(self.config.routines.tagging)(*deps)
        self.version: RoutineVersion = RoutineVersionFactory.create(self.config.routines.version)(*deps)
        self.changelog: RoutineChangelog = RoutineChangelogFactory.create(self.config.routines.changelog)(*deps)
        self.commiting: RoutineCommiting = RoutineCommitingFactory.create(self.config.routines.commiting)(*deps)
        self.file_updater: RoutineFileUpdater = RoutineFileUpdaterFactory.create(self.config.routines.file_updater)(*deps)
        self.commit_message: RoutineCommitMessage = RoutineCommitMessageFactory.create(self.config.routines.commit_message)(*deps)
        self.prefix_tag_with_v: RoutinePrefixTagWithV = RoutinePrefixTagWithVFactory.create(self.config.routines.prefix_tag_with_v)(*deps)
        self.should_contribute: RoutineShouldContribute = RoutineShouldContributeFactory.create(self.config.routines.should_contribute)(*deps)

    def versionise(self) -> VersioningResult:
        versions = self.version.run()
        return VersioningResult(
            versions=versions,
            commit_message=self.commit_message.run(versions.new),
            prefix_tag_with_v=self.prefix_tag_with_v.run(versions),
            updated_files=self.file_updater.run(versions),
            changelog=self.changelog.run(versions.new),
        )

    def contribute(self, result: VersioningResult) -> None:
        if not self.should_contribute.run(result):
            return

        self.commiting.run(result)
        self.tagging.run(result)

    def run(self) -> None:
        self.contribute(self.versionise())
