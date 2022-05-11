from dataclasses import dataclass, field

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.commit_utils.bump_tag_utils import IncrementTagUtils
from gitversioniser.domain.repository.commit_utils.commit_tag_utils import CommitTagUtils
from gitversioniser.domain.repository.commit_utils.version_tag_utils import VersionTagUtils


@dataclass
class Summary:
    config: Config = field(repr=False)
    value: str

    def __post_init__(self):
        self.bump_tag = IncrementTagUtils(self.config, self.value)
        self.commit_tag = CommitTagUtils(self.config, self.value)
        self.version_tag = VersionTagUtils(self.config, self.value)

    def __str__(self):
        return self.value
