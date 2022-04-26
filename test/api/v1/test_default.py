import unittest

from config.arguments import Arguments
from config.commit_tag import CommitTag
from config.config import Config
from config.increment import Increment
from helpers.changelog_category import ChangelogCategory
from helpers.version_bump import VersionBump


class TestDefaultConfig(unittest.TestCase):
    """
    Changing or removing any single line in this file means breaking the API (config) promise,
    thus must result in a major increment of the version of this repository.
    """

    def get_config(self) -> Config:
        arguments = Arguments.get_arguments()
        return Config(
            target_repository_path=arguments.target_directory,
            versioned_files=arguments.versioned_files,
            routines=arguments.routines,
        )

    def setUp(self):
        self.config: Config = self.get_config()

    def test_default_arguments_main(self):
        self.assertEqual(self.config.target_repository_path, '.')
        self.assertEqual(self.config.versioned_files, [])

    def test_default_arguments_routines(self):
        self.assertEqual(self.config.routines.version, 'last_gitversioniser_commit')
        self.assertEqual(self.config.routines.commit_message, 'prefix_tag')
        self.assertEqual(self.config.routines.file_updater, 'versionise_files')
        self.assertEqual(self.config.routines.contribution, 'push_main_amend')
        self.assertEqual(self.config.routines.changelog, 'commit_pattern')

    def test_default_configuration_credentials(self):
        self.assertEqual(self.config.credentials.username, "git@versioniser.com")
        self.assertEqual(self.config.credentials.email, "GitVersioniser")

    def test_default_configuration_patterns_increments(self):
        self.assertEqual(self.config.patterns.increments.major, Increment("#major", VersionBump.MAJOR))
        self.assertEqual(self.config.patterns.increments.minor, Increment("#minor", VersionBump.MINOR))
        self.assertEqual(self.config.patterns.increments.patch, Increment("#minor", VersionBump.PATCH))

    def test_default_configuration_patterns_commit_tags(self):
        self.assertEqual(self.config.patterns.commit_tags.added, CommitTag("A:", ChangelogCategory.ADDED))
        self.assertEqual(self.config.patterns.commit_tags.changed, CommitTag("C:", ChangelogCategory.CHANGED))
        self.assertEqual(self.config.patterns.commit_tags.deprecated, CommitTag("D:", ChangelogCategory.DEPRECATED))
        self.assertEqual(self.config.patterns.commit_tags.removed, CommitTag("R:", ChangelogCategory.REMOVED))
        self.assertEqual(self.config.patterns.commit_tags.security, CommitTag("S:", ChangelogCategory.SECURITY))
        self.assertEqual(self.config.patterns.commit_tags.fixed, CommitTag("F:", ChangelogCategory.FIXED))
