from dataclasses import dataclass, field

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.commit_utils.bump_tag_utils import IncrementTagUtils
from gitversioniser.domain.repository.commit_utils.commit_tag_utils import CommitTagUtils
from gitversioniser.domain.repository.commit_utils.version_tag_utils import VersionTagUtils


@dataclass
class Message:
    """
    Message:
        [summary]       | C: Shortened the foo in the bar width
        ...             |
        [description]   | It looked bad on small resolution.
        ...             |
        [footer]        | Issue: #123
    """
    config: Config = field(repr=False)
    value: str

    def __post_init__(self):
        self.summary: str = self.value.split('\n', 1)[0]
        self.footer: str = self.value.split('\n', 1)[-1]
        self.description: str = self.value.replace(self.summary, '').lstrip().replace(self.footer, '').rstrip()

        self.increment_tag = IncrementTagUtils(self.config, self.value)
        self.commit_tag = CommitTagUtils(self.config, self.value)
        self.version_tag = VersionTagUtils(self.config, self.value)

    def __str__(self):
        return self.value
