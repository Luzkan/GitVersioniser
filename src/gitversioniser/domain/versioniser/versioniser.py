from git.repo import Repo

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.git_repository import GitRepository
from gitversioniser.domain.versioniser.routines.changelog import RoutineChangelogFactory
from gitversioniser.domain.versioniser.routines.commit_message.factory import RoutineCommitMessageFactory
from gitversioniser.domain.versioniser.routines.commiting import RoutineCommitingFactory
from gitversioniser.domain.versioniser.routines.file_updater import RoutineFileUpdaterFactory
from gitversioniser.domain.versioniser.routines.manager import RoutineManager
from gitversioniser.domain.versioniser.routines.prefix_tag_with_v import RoutinePrefixTagWithVFactory
from gitversioniser.domain.versioniser.routines.should_contribute import RoutineShouldContributeFactory
from gitversioniser.domain.versioniser.routines.tagging import RoutineTaggingFactory
from gitversioniser.domain.versioniser.routines.version import RoutineVersionFactory


class Versioniser:
    def __init__(self, config: Config) -> None:
        deps: tuple[Config, GitRepository] = (config, GitRepository(config, _repo=Repo(config.target_repository_path)))
        self.routine_manager = RoutineManager(
            tagging=RoutineTaggingFactory.create(config.routines.tagging)(*deps),
            version=RoutineVersionFactory.create(config.routines.version)(*deps),
            changelog=RoutineChangelogFactory.create(config.routines.changelog)(*deps),
            commiting=RoutineCommitingFactory.create(config.routines.commiting)(*deps),
            file_updater=RoutineFileUpdaterFactory.create(config.routines.file_updater)(*deps),
            commit_message=RoutineCommitMessageFactory(config.routines.commit_message).create(deps),
            prefix_tag_with_v=RoutinePrefixTagWithVFactory.create(config.routines.prefix_tag_with_v)(*deps),
            should_contribute=RoutineShouldContributeFactory.create(config.routines.should_contribute)(*deps)
        )

    def run(self) -> None:
        self.routine_manager.run()

# [add_version_tag_to_summary]      Prefix                      | Suffix                    | Null
#   -                               Full                        | FullButOnlyDigits         | MajorMinorPatch   | MajorMinorPatchPrerelease
# [summarize_changes_in_summary]    LettersAndSummary           | EmojisAndSummary          | Summary
# [list_changes_in_description]     CommitTagLetterAndMessage   | CommitTagEmojiAndMessage  | Description
