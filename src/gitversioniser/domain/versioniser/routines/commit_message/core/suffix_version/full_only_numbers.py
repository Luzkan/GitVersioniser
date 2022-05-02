from dataclasses import dataclass

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class SuffixVersionFullOnlyNumbers(RoutineCommitMessage):
    def new_commit_message(self, new_version: SemverTag) -> str:
        return f"{self.repo.commits.latest.message.value.rstrip()} [`{new_version.to_acronym()}`]"

    @staticmethod
    def _filter_only_digits(version: str) -> str:
        return "".join(filter(str.isdigit, version))

    @staticmethod
    def factory_name() -> str:
        return 'suffix_version_full_only_numbers'
