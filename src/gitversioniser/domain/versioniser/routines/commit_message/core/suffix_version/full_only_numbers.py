from dataclasses import dataclass

from semver import VersionInfo

from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class SuffixVersionFullOnlyNumbers(RoutineCommitMessage):
    def run(self, new_version: VersionInfo) -> str:
        version_tag = f"{str(new_version.major)}.{str(new_version.minor)}.{str(new_version.patch)}"
        if new_version.prerelease:
            version_tag += f"-{self._filter_only_digits(str(new_version.prerelease))}"
        if new_version.build:
            version_tag += f"+{self._filter_only_digits(str(new_version.build))}"
        return f"{self.repo.commits.latest.summary} [`{version_tag}`]"

    @staticmethod
    def _filter_only_digits(version: str) -> str:
        return "".join(filter(str.isdigit, version))

    @staticmethod
    def factory_name() -> str:
        return 'suffix_version_full_only_numbers'
