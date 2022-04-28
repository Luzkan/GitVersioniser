from dataclasses import dataclass

from gitversioniser.helpers.types import (
    ROUTINE_CHANGELOG_TYPE,
    ROUTINE_COMMIT_MESSAGE_TYPE,
    ROUTINE_CONTRIBUTION_TYPE,
    ROUTINE_FILE_UPDATER_TYPE,
    ROUTINE_TAGGING_TYPE,
    ROUTINE_VERSION_TYPE,
)


@dataclass
class Routines:
    version: ROUTINE_VERSION_TYPE
    commit_message: ROUTINE_COMMIT_MESSAGE_TYPE
    commiting: ROUTINE_CONTRIBUTION_TYPE
    file_updater: ROUTINE_FILE_UPDATER_TYPE
    changelog: ROUTINE_CHANGELOG_TYPE
    tagging: ROUTINE_TAGGING_TYPE
