from dataclasses import dataclass

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class PrefixVersionFullOnlyNumbers(RoutineCommitMessage):
    def new_commit_message(self, new_version: SemverTag) -> str:
        return f"[`{new_version.to_acronym()}`] {self.repo.commits.latest.message.value.rstrip()}"

    @staticmethod
    def _filter_only_digits(version: str) -> str:
        return "".join(filter(str.isdigit, version))

    @staticmethod
    def factory_name() -> str:
        return 'prefix_version_full_only_numbers'
