import argparse
from dataclasses import dataclass

from gitversioniser.config.patterns import CommitPatterns
from gitversioniser.config.routines.commit_message import CommitMessageArguments
from gitversioniser.config.routines.routines import Routines


@dataclass(frozen=True)
class Arguments:
    target_directory: str
    versioned_files: list[str]
    routines: Routines
    patterns: CommitPatterns

    @staticmethod
    def get_arguments() -> 'Arguments':
        parser = argparse.ArgumentParser(description="GitVersioniser [0.6.0-rc.1]")
        parser.add_argument(
            "-d", "--target_directory", default='.',
            help="(Setting) Path to repository which shall be versionised. (default: %(default)s)"
        )

        Arguments.add_version(parser)
        Arguments.add_prefix_with_v(parser)
        Arguments.add_tagging(parser)
        Arguments.add_commiting(parser)
        Arguments.add_should_contibute(parser)
        Arguments.add_file_updater(parser)
        Arguments.add_commit_pattern(parser)
        Arguments.add_routine_commit_message(parser)
        Arguments.add_changelog(parser)

        parsed_arguments = parser.parse_args()
        return Arguments(
            target_directory=parsed_arguments.target_directory,
            versioned_files=parsed_arguments.versioned_files,
            routines=Routines(
                changelog=parsed_arguments.routine_changelog,
                commit_message=CommitMessageArguments(
                    describe_changes=parsed_arguments.routine_commit_message_describe_changes,
                    format_version_tag=parsed_arguments.routine_commit_message_format_version_tag,
                    place_version_tag=parsed_arguments.routine_commit_message_place_version_tag,
                    summarize_changes=parsed_arguments.routine_commit_message_summarize_changes,
                ),
                commiting=parsed_arguments.routine_commiting,
                file_updater=parsed_arguments.routine_file_updater,
                should_contribute=parsed_arguments.routine_should_contribute,
                prefix_tag_with_v=parsed_arguments.routine_prefix_tag_with_v,
                tagging=parsed_arguments.routine_tagging,
                version=parsed_arguments.routine_version
            ),
            patterns=CommitPatterns.init_from_arguments(
                increment_tags=parsed_arguments.commit_pattern_increment_tags,
                change_tags=parsed_arguments.commit_pattern_change_tags,
            )
        )

    @staticmethod
    def add_commit_pattern(parser):
        parser.add_argument(
            "-cit", "--commit_pattern_increment_tags", default='HashtagExplicit',
            help="(Tags) Tags to look for in commit message for semver incrementation. (default: %(default)s)"
        )
        parser.add_argument(
            "-cct", "--commit_pattern_change_tags", default='ClassicChangelog',
            help="(Tags) Tags to look for in commit message for changelog entries creation. (default: %(default)s)"
        )

    @staticmethod
    def add_file_updater(parser):
        parser.add_argument(
            "-rfu", "--routine_file_updater", default='VersioniseFiles',
            help="(Routine) Decides which files will be versionised. (default: %(default)s)"
        )
        parser.add_argument(
            "-vf", "--versioned_files", default=list(), nargs='+',
            help="(Setting) Decides which files will be versionised. (default: %(default)s)"
        )

    @staticmethod
    def add_routine_commit_message(parser):
        parser.add_argument(
            "-rcmdc", "--routine_commit_message_describe_changes", default='WithEmoji',
            help="(Routine) Decides about the descriptive summarization after first commit message line. (default: %(default)s)"
        )
        parser.add_argument(
            "-rcmfvt", "--routine_commit_message_format_version_tag", default='FullButOnlyDigits',
            help="(Routine) Decides the Version Tag string representation. (default: %(default)s)"
        )
        parser.add_argument(
            "-rcmpvt", "--routine_commit_message_place_version_tag", default='Prefix',
            help="(Routine) Decides the placement of version tag in commit message. (default: %(default)s)"
        )
        parser.add_argument(
            "-rcmsc", "--routine_commit_message_summarize_changes", default='WithEmojiCounted',
            help="(Routine) Decides the summarization of all changes in the first line of commit message. (default: %(default)s)"
        )

    @staticmethod
    def add_should_contibute(parser):
        parser.add_argument(
            "-rsc", "--routine_should_contribute", default='IfNewVersionIsBuildOrHigher',
            help="(Routine) When should the GitVersioniser contribute anything to the remote repository. (default: %(default)s)"
        )

    @staticmethod
    def add_commiting(parser):
        parser.add_argument(
            "-rc", "--routine_commiting", default='PushOriginAmend',
            help="(Routine) The way of contributing the GitVersioniser changes to remote repository. (default: %(default)s)"
        )

    @staticmethod
    def add_changelog(parser):
        parser.add_argument(
            "-rcl", "--routine_changelog", default='CommitChangeTags',
            help="(Routine) The way GitVersioniser will handle changelog. (default: %(default)s)"
        )

    @staticmethod
    def add_tagging(parser):
        parser.add_argument(
            "-rt", "--routine_tagging", default='Regular',
            help="(Routine) How should GitVersioniser tag the repository. (default: %(default)s)"
        )

    @staticmethod
    def add_prefix_with_v(parser):
        parser.add_argument(
            "-rptwv", "--routine_prefix_tag_with_v", default='Always',
            help="(Routine) When the tag should receive the 'v' letter as prefix. (default: %(default)s)"
        )

    @staticmethod
    def add_version(parser):
        parser.add_argument(
            "-rv", "--routine_version", default='VersionTagInCommitsTillLastGitVersioniserCommit',
            help="(Routine) The way the repository should be versionised. (default: %(default)s)"
        )
