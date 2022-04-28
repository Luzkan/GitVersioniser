import argparse
from dataclasses import dataclass

from gitversioniser.config.routines import Routines


@dataclass(frozen=True)
class Arguments:
    target_directory: str
    versioned_files: list[str]
    routines: Routines

    @staticmethod
    def get_arguments() -> 'Arguments':
        parser = argparse.ArgumentParser(description="GitVersioniser [0.1.0+build.2]")
        parser.add_argument(
            "-d", "--target_directory", default='.',
            help="(Setting) Path to repository which shall be versionised. (default: %(default)s)"
        )
        parser.add_argument(
            "-vf", "--versioned_files", default=list(), nargs='+',
            help="(Setting) Decides which files will be versionised. (default: %(default)s)"
        )
        parser.add_argument(
            "-rv", "--routine_version", default='last_gitversioniser_commit',
            help="(Routine) The way the repository should be versionised. (default: %(default)s)"
        )
        parser.add_argument(
            "-rcm", "--routine_commit_message", default='prefix_tag',
            help="(Routine) Decides how the Commit Message made by GitVersioniser will be made. (default: %(default)s)"
        )
        parser.add_argument(
            "-rfu", "--routine_file_updater", default='versionise_files',
            help="(Routine) Decides which files will be versionised. (default: %(default)s)"
        )
        parser.add_argument(
            "-rc", "--routine_commiting", default='push_main_amend',
            help="(Routine) The way of contributing the GitVersioniser changes to remote repository. (default: %(default)s)"
        )
        parser.add_argument(
            "-rcl", "--routine_changelog", default='commit_pattern',
            help="(Routine) The way GitVersioniser will handle changelog. (default: %(default)s)"
        )
        parser.add_argument(
            "-rt", "--routine_tagging", default='always',
            help="(Routine) When should GitVersioniser tag the repository. (default: %(default)s)"
        )
        parsed_arguments = parser.parse_args()
        return Arguments(
            target_directory=parsed_arguments.target_directory,
            versioned_files=parsed_arguments.versioned_files,
            routines=Routines(
                version=parsed_arguments.routine_version,
                commit_message=parsed_arguments.routine_commit_message,
                file_updater=parsed_arguments.routine_file_updater,
                commiting=parsed_arguments.routine_commiting,
                changelog=parsed_arguments.routine_changelog,
                tagging=parsed_arguments.routine_tagging
            ),
        )
