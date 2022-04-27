from dataclasses import dataclass
from pathlib import Path


@dataclass
class ChangelogFinder:
    def get_changelog(self) -> Path:
        if not self.is_changelog_present():
            return self.init_changelog_template()
        return self.get_existing_changelog()

    def is_changelog_present(self) -> bool:
        return len(self._find_changelog()) > 0

    def get_existing_changelog(self) -> Path:
        return self._find_changelog()[0]

    def init_changelog_template(self) -> Path:
        def load_template() -> str:
            with open(Path('/src/gitversioniser/domain/versioniser/routines/changelog/init_template.md'), 'r') as f:
                return f.read()

        with open(Path('./CHANGELOG.md'), 'w') as f:
            f.write(load_template())
        return Path('./CHANGELOG.md')

    def _find_changelog(self) -> list[Path]:
        return list(Path('.').glob('**/CHANGELOG.md'))
