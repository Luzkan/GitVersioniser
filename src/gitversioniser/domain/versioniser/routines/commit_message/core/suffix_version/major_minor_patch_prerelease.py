from dataclasses import dataclass

from semver import VersionInfo

from gitversioniser.domain.versioniser.routines.commit_message.abstract import RoutineCommitMessage


@dataclass
class SuffixVersionMajorMinorPatchPrerelease(RoutineCommitMessage):
    def run(self, new_version: VersionInfo) -> str:
        version_tag = f"{str(new_version.major)}.{str(new_version.minor)}.{str(new_version.patch)}"
        if new_version.prerelease:
            version_tag += f"-{str(new_version.prerelease)}"
        return f"{self.target_repo.commits.latest.summary} [`{version_tag}`]"

    @staticmethod
    def factory_name() -> str:
        return 'suffix_version_major_minor_patch_prerelease'
