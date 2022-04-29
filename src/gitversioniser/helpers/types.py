from typing import Literal


ROUTINE_VERSION_TYPE = Literal[
    "last_commit",
    "last_gitversioniser_commit"
]
ROUTINE_COMMIT_MESSAGE_TYPE = Literal[
    "null",
    "prefix_version_full",
    "prefix_version_major_minor_patch",
    "prefix_version_major_minor_patch_prerelease",
    "suffix_version",
    "suffix_version_major_minor_patch",
    "suffix_version_major_minor_patch_prerelease",
]
ROUTINE_COMMITING_TYPE = Literal[
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
