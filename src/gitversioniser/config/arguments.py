import argparse
from dataclasses import dataclass

from gitversioniser.config.commit_change_tags.factory import CommitChangeTagsFactory
from gitversioniser.config.commit_increment_tags.factory import CommitIncrementTagsFactory
from gitversioniser.config.patterns import Patterns
from gitversioniser.config.routines import Routines


@dataclass(frozen=True)
class Arguments:
    target_directory: str
    versioned_files: list[str]
    routines: Routines
    patterns: Patterns

    @staticmethod
    def get_arguments() -> 'Arguments':
        parser = argparse.ArgumentParser(description="GitVersioniser [0.5.3]")
        parser.add_argument(
            "-d", "--target_directory", default='.',
            help="(Setting) Path to repository which shall be versionised. (default: %(default)s)"
        )
        parser.add_argument(
            "-vf", "--versioned_files", default=list(), nargs='+',
            help="(Setting) Decides which files will be versionised. (default: %(default)s)"
        )
        parser.add_argument(
            "-rv", "--routine_version", default='VersionTagInCommitsTillLastGitVersioniserCommit',
            help="(Routine) The way the repository should be versionised. (default: %(default)s)"
        )
        parser.add_argument(
            "-cit", "--commit_increment_tags", default='HashtagExplicit',
            help="(Tags) Tags to look for in commit message for semver incrementation. (default: %(default)s)"
        )
        parser.add_argument(
            "-cct", "--commit_change_tags", default='ClassicChangelog',
            help="(Tags) Tags to look for in commit message for changelog entries creation. (default: %(default)s)"
        )
        parser.add_argument(
            "-rcm", "--routine_commit_message", default='PrefixVersionFull',
            help="(Routine) Decides how the Commit Message made by GitVersioniser will be made. (default: %(default)s)"
        )
        parser.add_argument(
            "-rfu", "--routine_file_updater", default='VersioniseFiles',
            help="(Routine) Decides which files will be versionised. (default: %(default)s)"
        )
        parser.add_argument(
            "-rc", "--routine_commiting", default='PushOriginAmend',
            help="(Routine) The way of contributing the GitVersioniser changes to remote repository. (default: %(default)s)"
        )
        parser.add_argument(
            "-rptwv", "--routine_prefix_tag_with_v", default='Always',
            help="(Routine) When the tag should receive the 'v' letter as prefix. (default: %(default)s)"
        )
        parser.add_argument(
            "-rsc", "--routine_should_contribute", default='IfNewVersionIsBuildOrHigher',
            help="(Routine) When should the GitVersioniser contribute anything to the remote repository. (default: %(default)s)"
        )
        parser.add_argument(
            "-rcl", "--routine_changelog", default='CommitChangeTags',
            help="(Routine) The way GitVersioniser will handle changelog. (default: %(default)s)"
        )
        parser.add_argument(
            "-rt", "--routine_tagging", default='Regular',
            help="(Routine) How should GitVersioniser tag the repository. (default: %(default)s)"
        )
        parsed_arguments = parser.parse_args()
        return Arguments(
            target_directory=parsed_arguments.target_directory,
            versioned_files=parsed_arguments.versioned_files,
            routines=Routines(
                changelog=parsed_arguments.routine_changelog,
                commit_message=parsed_arguments.routine_commit_message,
                commiting=parsed_arguments.routine_commiting,
                file_updater=parsed_arguments.routine_file_updater,
                should_contribute=parsed_arguments.routine_should_contribute,
                prefix_tag_with_v=parsed_arguments.routine_prefix_tag_with_v,
                tagging=parsed_arguments.routine_tagging,
                version=parsed_arguments.routine_version
            ),
            patterns=Patterns(
                increments=CommitIncrementTagsFactory.create(parsed_arguments.commit_increment_tags)(),
                commit_tags=CommitChangeTagsFactory.create(parsed_arguments.commit_change_tags)(),
            )
        )
