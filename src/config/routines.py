from dataclasses import dataclass

from helpers.types import (
    ROUTINE_CHANGELOG_TYPE,
    ROUTINE_COMMIT_MESSAGE_TYPE,
    ROUTINE_CONTRIBUTION_TYPE,
    ROUTINE_FILE_UPDATER_TYPE,
    ROUTINE_VERSION_TYPE,
)


@dataclass
class Routines:
    version: ROUTINE_VERSION_TYPE
    commit_message: ROUTINE_COMMIT_MESSAGE_TYPE
    contribution: ROUTINE_CONTRIBUTION_TYPE
    file_updater: ROUTINE_FILE_UPDATER_TYPE
    changelog: ROUTINE_CHANGELOG_TYPE
