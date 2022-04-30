from pathlib import Path


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
        def load_template(template: Path) -> str:
            if not template.exists():
                with open(Path(f'.{template}'), 'r') as f:
                    return f.read()
            with open(template, 'r') as f:
                return f.read()

        with open(Path('./CHANGELOG.md'), 'w') as f:
            f.write(load_template(Path('/src/gitversioniser/domain/versioniser/routines/changelog/utils/init_template.md')))
        return Path('./CHANGELOG.md')

    def _find_changelog(self) -> list[Path]:
        return list(Path('.').glob('./**/CHANGELOG.md'))
