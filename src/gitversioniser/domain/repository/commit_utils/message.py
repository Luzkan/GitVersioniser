from dataclasses import dataclass, field

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.commit_utils.bump_tag_utils import IncrementTagUtils
from gitversioniser.domain.repository.commit_utils.commit_tag_utils import CommitTagUtils
from gitversioniser.domain.repository.commit_utils.summary import Summary
from gitversioniser.domain.repository.commit_utils.version_tag_utils import VersionTagUtils


@dataclass
class Message:
    config: Config = field(repr=False)
    value: str
    summary: Summary = field(init=False)
    increment_tag: IncrementTagUtils = field(init=False)
    commit_tag: CommitTagUtils = field(init=False)
    version_tag: VersionTagUtils = field(init=False)

    def __post_init__(self):
        self.summary = Summary(self.config, self.value.split('\n', 1)[0])
        self.increment_tag = IncrementTagUtils(self.config, self.value)
        self.commit_tag = CommitTagUtils(self.config, self.value)
        self.version_tag = VersionTagUtils(self.config, self.value)

    def __str__(self):
        return self.value
