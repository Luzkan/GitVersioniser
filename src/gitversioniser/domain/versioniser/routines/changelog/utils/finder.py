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

    @staticmethod
    def init_changelog_template() -> Path:
        def load_template(template: Path) -> str:
            with open(Path(f'.{template}') if not template.exists() else template, 'r', encoding='utf-8') as template_file:
                return template_file.read()

        with open(Path('./CHANGELOG.md'), 'w', encoding='utf-8') as changelog_file:
            changelog_file.write(load_template(Path('/src/gitversioniser/domain/versioniser/routines/changelog/utils/init_template.md')))
        return Path('./CHANGELOG.md')

    @staticmethod
    def _find_changelog() -> list[Path]:
        return list(Path('.').glob('./**/CHANGELOG.md'))
