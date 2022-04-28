from typing import Literal


ROUTINE_VERSION_TYPE = Literal[
    "last_commit",
    "last_gitversioniser_commit"
]
ROUTINE_COMMIT_MESSAGE_TYPE = Literal[
    "null",
    "prefix_tag",
    "suffix_tag"
]
ROUTINE_CONTRIBUTION_TYPE = Literal[
    "null",
    "push_main_amend",
    "push_main_new"
]
ROUTINE_TAGGING_TYPE = Literal[
    "null",
    "always",
    "if_patch_or_higher",
    "if_prerelease_or_higher"
]
ROUTINE_FILE_UPDATER_TYPE = Literal[
    "null",
    "versionise_files"
]
ROUTINE_CHANGELOG_TYPE = Literal[
    "null",
    "commit_pattern"
]
