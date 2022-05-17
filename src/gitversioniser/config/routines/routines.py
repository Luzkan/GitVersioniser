from dataclasses import dataclass

from gitversioniser.config.routines.commit_message import CommitMessageArguments
from gitversioniser.helpers.types import (
    ROUTINE_CHANGELOG_TYPE,
    ROUTINE_COMMITING_TYPE,
    ROUTINE_FILE_UPDATER_TYPE,
    ROUTINE_PREFIX_TAG_WITH_V,
    ROUTINE_SHOULD_CONTRIBUTE,
    ROUTINE_TAGGING_TYPE,
    ROUTINE_VERSION_TYPE,
)


@dataclass(frozen=True)
class Routines:
    changelog: ROUTINE_CHANGELOG_TYPE
    commit_message: CommitMessageArguments
    commiting: ROUTINE_COMMITING_TYPE
    file_updater: ROUTINE_FILE_UPDATER_TYPE
    prefix_tag_with_v: ROUTINE_PREFIX_TAG_WITH_V
    should_contribute: ROUTINE_SHOULD_CONTRIBUTE
    tagging: ROUTINE_TAGGING_TYPE
    version: ROUTINE_VERSION_TYPE
