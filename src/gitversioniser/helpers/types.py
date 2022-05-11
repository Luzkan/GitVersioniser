from typing import Literal


COMMIT_CHANGE_TAG_TYPE = Literal[
    "ClassicChangelog",
]
COMMIT_INCREMENT_TAG_TYPE = Literal[
    "HashtagExplicit",
]
ROUTINE_VERSION_TYPE = Literal[
    "VersionTagInLastCommit",
    "VersionTagInCommitsTillLastGitVersioniserCommit",
]
ROUTINE_COMMIT_MESSAGE_TYPE = Literal[
    "Null",
    "PrefixVersionFull",
    "PrefixVersionFullButOnlyDigits",
    "PrefixVersionMajorMinorPatch",
    "PrefixVersionMajorMinorPatchPrerelease",
    "SuffixVersionFull",
    "SuffixVersionFullButOnlyDigits",
    "SuffixVersionMajorMinorPatch",
    "SuffixVersionMajorMinorPatchPrerelease",
]
ROUTINE_COMMITING_TYPE = Literal[
    "Null",
    "PushOriginAmend",
    "PushOriginNewCommit",
]
ROUTINE_TAGGING_TYPE = Literal[
    "Force",
    "Regular",
    "Never",
]
ROUTINE_SHOULD_CONTRIBUTE = Literal[
    "Never",
    "IfNewVersionIsBuildOrHigher",
    "IfNewVersionIsPatchOrHigher",
    "IfNewVersionIsPrereleaseOrHigher",
]
ROUTINE_PREFIX_TAG_WITH_V = Literal[
    "Never",
    "IfNewVersionIsBuildOrHigher",
    "IfNewVersionIsPatchOrHigher",
    "IfNewVersionIsPrereleaseOrHigher",
    "Always",
]
ROUTINE_FILE_UPDATER_TYPE = Literal[
    "Null",
    "VersioniseFiles",
]
ROUTINE_CHANGELOG_TYPE = Literal[
    "Null",
    "CommitChangeTags",
    "LastCommitMessageAsDescription",
]
