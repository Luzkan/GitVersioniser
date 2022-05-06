from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.changelog import RoutineChangelog
from gitversioniser.domain.versioniser.routines.commit_message import RoutineCommitMessage
from gitversioniser.domain.versioniser.routines.commiting import RoutineCommiting
from gitversioniser.domain.versioniser.routines.file_updater import RoutineFileUpdater
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v import RoutinePrefixTagWithV
from gitversioniser.domain.versioniser.routines.should_contribute import RoutineShouldContribute
from gitversioniser.domain.versioniser.routines.tagging import RoutineTagging
from gitversioniser.domain.versioniser.routines.version import RoutineVersion
from gitversioniser.domain.versioniser.utils.routine_result import VersioningResult


@dataclass(frozen=True)
class RoutineManager:
    tagging: RoutineTagging
    version: RoutineVersion
    changelog: RoutineChangelog
    commiting: RoutineCommiting
    file_updater: RoutineFileUpdater
    commit_message: RoutineCommitMessage
    prefix_tag_with_v: RoutinePrefixTagWithV
    should_contribute: RoutineShouldContribute

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
