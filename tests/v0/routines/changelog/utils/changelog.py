from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from gitversioniser.domain.versioniser.routines.changelog.abstract import RoutineChangelog
from gitversioniser.domain.versioniser.routines.changelog.utils.finder import ChangelogFinder


@dataclass
class TestChangelogManager:
    routine: RoutineChangelog
    test_directory_name: str

    def get_changelog_generated_content(self) -> str:
        changelog_generated: Path = ChangelogFinder().get_changelog()
        with open(changelog_generated, 'r') as f:
            return f.read().replace(datetime.now().strftime('%Y-%m-%d'), '[date]')

    def get_changelog_test_content(self, name: str) -> str:
        changelog_test_output: Path = list(Path('.').glob(f'./**/{self.test_directory_name}/{name}.md'))[0]
        with open(changelog_test_output, 'r') as f:
            return f.read()

    def rename_changelog_temporarily(self):
        self.old_changelog: Path = ChangelogFinder().get_changelog()
        self.old_changelog = self.old_changelog.rename(self.old_changelog.parent / 'old_CHANGELOG.md')

    def bring_back_old_changelog(self):
        generated_changelog: Path = ChangelogFinder().get_changelog()
        generated_changelog.unlink()
        self.old_changelog.rename(self.old_changelog.parent / 'CHANGELOG.md')

    def delete_remotes(self):
        try:
            self.routine.target_repo.repo.delete_remote(self.routine.target_repo.repo.remote('origin'))
        except ValueError:
            pass

    def create_remotes(self):
        self.routine.target_repo.repo.create_remote('origin', 'https://github.com/Luzkan/GitVersioniserTest.git')
