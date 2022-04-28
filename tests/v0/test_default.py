from gitversioniser.config.commit_tag import CommitTag
from gitversioniser.config.increment import Increment
from gitversioniser.helpers.changelog_category import ChangelogCategory
from gitversioniser.helpers.version_bump import VersionBump
from tests.v0.utils.default_v0 import TestDefaultV0


class TestDefaultConfig(TestDefaultV0):
    def test_default_arguments_main(self):
        self.assertEqual(self.config.target_repository_path, '../gitversioniser_test/')
        self.assertEqual(self.config.versioned_files, [])

    def test_default_arguments_routines(self):
        self.assertEqual(self.config.routines.version, 'last_gitversioniser_commit')
        self.assertEqual(self.config.routines.commit_message, 'prefix_tag')
        self.assertEqual(self.config.routines.file_updater, 'versionise_files')
        self.assertEqual(self.config.routines.commiting, 'push_main_amend')
        self.assertEqual(self.config.routines.changelog, 'commit_pattern')

    def test_default_configuration_credentials(self):
        self.assertEqual(self.config.credentials.username, "GitVersioniser")
        self.assertEqual(self.config.credentials.email, "git@versioniser.com")

    def test_default_configuration_patterns_increments(self):
        self.assertEqual(self.config.patterns.increments.major, Increment("#major", VersionBump.MAJOR))
        self.assertEqual(self.config.patterns.increments.minor, Increment("#minor", VersionBump.MINOR))
        self.assertEqual(self.config.patterns.increments.patch, Increment("#patch", VersionBump.PATCH))

    def test_default_configuration_patterns_commit_tags(self):
        self.assertEqual(self.config.patterns.commit_tags.added, CommitTag("A:", ChangelogCategory.ADDED))
        self.assertEqual(self.config.patterns.commit_tags.changed, CommitTag("C:", ChangelogCategory.CHANGED))
        self.assertEqual(self.config.patterns.commit_tags.deprecated, CommitTag("D:", ChangelogCategory.DEPRECATED))
        self.assertEqual(self.config.patterns.commit_tags.removed, CommitTag("R:", ChangelogCategory.REMOVED))
        self.assertEqual(self.config.patterns.commit_tags.security, CommitTag("S:", ChangelogCategory.SECURITY))
        self.assertEqual(self.config.patterns.commit_tags.fixed, CommitTag("F:", ChangelogCategory.FIXED))
