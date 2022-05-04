from gitversioniser.config.commit_tag import CommitTag
from gitversioniser.helpers.changelog_category import ChangelogCategory
from tests.v0.default_scenario_v0 import TestDefaultScenarioV0


class TestDefaultConfigValues(TestDefaultScenarioV0):
    def test_default_arguments_main(self):
        self.assertEqual(self.config.target_repository_path, '../gitversioniser_test/')
        self.assertEqual(self.config.versioned_files, [])

    def test_default_arguments_routines(self):
        self.assertEqual(self.config.routines.version, 'commits_till_last_gitversioniser_commit')
        self.assertEqual(self.config.routines.commit_message, 'prefix_version_full')
        self.assertEqual(self.config.routines.file_updater, 'versionise_files')
        self.assertEqual(self.config.routines.commiting, 'push_origin_amend')
        self.assertEqual(self.config.routines.tagging, 'regular')
        self.assertEqual(self.config.routines.changelog, 'commit_pattern')

    def test_default_configuration_credentials(self):
        self.assertEqual(self.config.credentials.username, "GitVersioniser")
        self.assertEqual(self.config.credentials.email, "luzkan.gitversioniser@github.com")

    def test_default_configuration_patterns_increments(self):
        self.assertEqual(self.config.patterns.increments.major.pattern, '#major')
        self.assertEqual(self.config.patterns.increments.major.precedence, 1)
        self.assertEqual(self.config.patterns.increments.minor.pattern, '#minor')
        self.assertEqual(self.config.patterns.increments.minor.precedence, 1)
        self.assertEqual(self.config.patterns.increments.patch.pattern, '#patch')
        self.assertEqual(self.config.patterns.increments.patch.precedence, 1)
        self.assertEqual(self.config.patterns.increments.alpha.pattern, '#alpha')
        self.assertEqual(self.config.patterns.increments.alpha.precedence, 2)
        self.assertEqual(self.config.patterns.increments.beta.pattern, '#beta')
        self.assertEqual(self.config.patterns.increments.beta.precedence, 3)
        self.assertEqual(self.config.patterns.increments.prerelease.pattern, '#prerelease')
        self.assertEqual(self.config.patterns.increments.prerelease.precedence, 4)
        self.assertEqual(self.config.patterns.increments.finalized.pattern, '#fin')
        self.assertEqual(self.config.patterns.increments.finalized.precedence, 9)

    def test_default_configuration_patterns_commit_tags(self):
        self.assertEqual(self.config.patterns.commit_tags.added, CommitTag("A:", ChangelogCategory.ADDED))
        self.assertEqual(self.config.patterns.commit_tags.changed, CommitTag("C:", ChangelogCategory.CHANGED))
        self.assertEqual(self.config.patterns.commit_tags.deprecated, CommitTag("D:", ChangelogCategory.DEPRECATED))
        self.assertEqual(self.config.patterns.commit_tags.removed, CommitTag("R:", ChangelogCategory.REMOVED))
        self.assertEqual(self.config.patterns.commit_tags.security, CommitTag("S:", ChangelogCategory.SECURITY))
        self.assertEqual(self.config.patterns.commit_tags.fixed, CommitTag("F:", ChangelogCategory.FIXED))
