from typing import Literal


ROUTINE_VERSION_TYPE = Literal[
    "last_commit",
    "commits_till_last_gitversioniser_commit",
]
ROUTINE_COMMIT_MESSAGE_TYPE = Literal[
    "null",
    "prefix_version_full",
    "prefix_version_full_only_numbers",
    "prefix_version_major_minor_patch",
    "prefix_version_major_minor_patch_prerelease",
    "suffix_version",
    "suffix_version_full_only_numbers",
    "suffix_version_major_minor_patch",
    "suffix_version_major_minor_patch_prerelease",
]
ROUTINE_COMMITING_TYPE = Literal[
    "null",
    "push_origin_amend",
    "push_origin_new_commit",
]
ROUTINE_TAGGING_TYPE = Literal[
    "force",
    "regular",
    "never",
]
ROUTINE_SHOULD_CONTRIBUTE = Literal[
    "never",
    "if_build_or_higher",
    "if_patch_or_higher",
    "if_prerelease_or_higher",
]
ROUTINE_PREFIX_TAG_WITH_V = Literal[
    "never",
    "if_build_or_higher",
    "if_patch_or_higher",
    "if_prerelease_or_higher",
    "always",
]
ROUTINE_FILE_UPDATER_TYPE = Literal[
    "null",
    "versionise_files",
]
ROUTINE_CHANGELOG_TYPE = Literal[
    "null",
    "commit_pattern",
    "last_commit_message_as_description",
]
