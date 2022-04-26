from typing import Literal


ROUTINE_VERSION_TYPE = \
    Literal["last_commit"] | \
    Literal["last_gitversioniser_commit"]
ROUTINE_COMMIT_MESSAGE_TYPE = \
    Literal["null"] | \
    Literal["prefix_tag"] | \
    Literal["suffix_tag"]
ROUTINE_CONTRIBUTION_TYPE = \
    Literal["null"] | \
    Literal["push_main_amend"] |\
    Literal["push_main_new"]
ROUTINE_FILE_UPDATER_TYPE = \
    Literal["null"] | \
    Literal["versionise_files"]
ROUTINE_CHANGELOG_TYPE = \
    Literal["null"] | \
    Literal["commit_pattern"]
