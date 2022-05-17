from gitversioniser.config.patterns.commit_change_tags.commit_tag import CommitTag
from gitversioniser.helpers.changelog_category import ChangelogCategory
from tests.v0.default_scenario_v0 import TestDefaultScenarioV0


class TestDefaultConfigValues(TestDefaultScenarioV0):
    def test_default_arguments_main(self):
        self.assertEqual(self.config.target_repository_path, '../gitversioniser_test/')
        self.assertEqual(self.config.versioned_files, [])

    def test_default_arguments_routines(self):
        self.assertEqual(self.config.routines.version, 'VersionTagInCommitsTillLastGitVersioniserCommit')
        # self.assertEqual(self.config.routines.commit_message, 'PrefixVersionFull')
        self.assertEqual(self.config.routines.file_updater, 'VersioniseFiles')
        self.assertEqual(self.config.routines.commiting, 'PushOriginAmend')
        self.assertEqual(self.config.routines.tagging, 'Regular')
        self.assertEqual(self.config.routines.changelog, 'CommitChangeTags')

    def test_default_configuration_credentials(self):
        self.assertEqual(self.config.credentials.username, "GitVersioniser")
        self.assertEqual(self.config.credentials.email, "luzkan.gitversioniser@github.com")

    def test_default_configuration_patterns_increments(self):
        self.assertEqual(self.config.commit_patterns.increment_tags.major.pattern, '#major')
        self.assertEqual(self.config.commit_patterns.increment_tags.major.precedence, 1)
        self.assertEqual(self.config.commit_patterns.increment_tags.minor.pattern, '#minor')
        self.assertEqual(self.config.commit_patterns.increment_tags.minor.precedence, 1)
        self.assertEqual(self.config.commit_patterns.increment_tags.patch.pattern, '#patch')
        self.assertEqual(self.config.commit_patterns.increment_tags.patch.precedence, 1)
        self.assertEqual(self.config.commit_patterns.increment_tags.alpha.pattern, '#alpha')
        self.assertEqual(self.config.commit_patterns.increment_tags.alpha.precedence, 2)
        self.assertEqual(self.config.commit_patterns.increment_tags.beta.pattern, '#beta')
        self.assertEqual(self.config.commit_patterns.increment_tags.beta.precedence, 3)
        self.assertEqual(self.config.commit_patterns.increment_tags.prerelease.pattern, '#prerelease')
        self.assertEqual(self.config.commit_patterns.increment_tags.prerelease.precedence, 4)
        self.assertEqual(self.config.commit_patterns.increment_tags.finalized.pattern, '#fin')
        self.assertEqual(self.config.commit_patterns.increment_tags.finalized.precedence, 9)

    def test_default_configuration_patterns_commit_tags(self):
        self.assertEqual(self.config.commit_patterns.change_tags.added, CommitTag("A:", ChangelogCategory.ADDED, "✨"))
        self.assertEqual(self.config.commit_patterns.change_tags.fixed, CommitTag("F:", ChangelogCategory.FIXED, "🛠️"))
        self.assertEqual(self.config.commit_patterns.change_tags.changed, CommitTag("C:", ChangelogCategory.CHANGED, "🔸"))
        self.assertEqual(self.config.commit_patterns.change_tags.removed, CommitTag("R:", ChangelogCategory.REMOVED, "🗑️"))
        self.assertEqual(self.config.commit_patterns.change_tags.security, CommitTag("S:", ChangelogCategory.SECURITY, "🔐"))
        self.assertEqual(self.config.commit_patterns.change_tags.deprecated, CommitTag("D:", ChangelogCategory.DEPRECATED, "🔚"))
