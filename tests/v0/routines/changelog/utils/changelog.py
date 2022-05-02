from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from gitversioniser.domain.versioniser.routines.changelog.abstract import RoutineChangelog
from gitversioniser.domain.versioniser.routines.changelog.utils.finder import ChangelogFinder


@dataclass
class TestChangelogManager:
    routine: RoutineChangelog
    test_directory_name: str

    @staticmethod
    def get_changelog_generated_content() -> str:
        changelog_generated: Path = ChangelogFinder().get_changelog()
        with open(changelog_generated, 'r', encoding='utf-8') as changelog_file:
            return changelog_file.read().replace(datetime.now().strftime('%Y-%m-%d'), '[date]')

    def get_changelog_test_content(self, name: str) -> str:
        changelog_test_output: Path = list(Path('.').glob(f'./**/{self.test_directory_name}/{name}.md'))[0]
        with open(changelog_test_output, 'r', encoding='utf-8') as changelog_file:
            return changelog_file.read()

    def rename_changelog_temporarily(self):
        self.old_changelog: Path = ChangelogFinder().get_changelog()
        self.old_changelog = self.old_changelog.rename(self.old_changelog.parent / 'old_CHANGELOG.md')

    def bring_back_old_changelog(self):
        generated_changelog: Path = ChangelogFinder().get_changelog()
        generated_changelog.unlink()
        self.old_changelog.rename(self.old_changelog.parent / 'CHANGELOG.md')
