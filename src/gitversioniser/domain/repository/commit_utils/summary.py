from dataclasses import dataclass, field

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.commit_utils.bump_tag import BumpTagUtils
from gitversioniser.domain.repository.commit_utils.commit_tag import CommitTagUtils
from gitversioniser.domain.repository.commit_utils.version_tag import VersionTagUtils


@dataclass
class Summary:
    config: Config
    value: str
    bump_tag: BumpTagUtils = field(init=False)
    commit_tag: CommitTagUtils = field(init=False)
    version_tag: VersionTagUtils = field(init=False)

    def __post_init__(self):
        self.bump_tag = BumpTagUtils(self.config, self.value)
        self.commit_tag = CommitTagUtils(self.config, self.value)
        self.version_tag = VersionTagUtils(self.config, self.value)

    def __str__(self):
        return self.value