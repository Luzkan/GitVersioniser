from typing import Literal


COMMIT_CHANGE_TAG_TYPE = Literal[
    "AngularCommits",
    "ClassicChangelog",
    "ClassicChangelogExtended",
    "ConventionalCommits",
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
ROUTINE_COMMIT_MESSAGE_DESCRIBE_CHANGES = Literal[
    "Null",
    "WithEmoji",
    "WithLetters",
]
ROUTINE_COMMIT_MESSAGE_FORMAT_VERSION_TAG = Literal[
    "Full",
    "FullButOnlyDigits",
    "MajorMinorPatch",
    "MajorMinorPatchPrerelease",
]
ROUTINE_COMMIT_MESSAGE_PLACE_VERSION_TAG = Literal[
    "Null",
    "Prefix",
    "Suffix",
]
ROUTINE_COMMIT_MESSAGE_SUMMARIZE_CHANGES = Literal[
    "Null",
    "WithEmojiSymbolic",
    "WithEmojiCounted",
    "WithLetters",
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
