from dataclasses import dataclass

from git.repo import Repo

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.commits import Commits
from gitversioniser.domain.repository.files import Files
from gitversioniser.domain.repository.remote import Remote
from gitversioniser.domain.repository.tags import Tags


@dataclass
class GitRepository:
    config: Config
    _repo: Repo

    def __post_init__(self):
        self.files = Files(self._repo)
        self.remote = Remote(self._repo)
        self.tags = Tags(self._repo)
        self.commits = Commits(self.config, self._repo)

    @property
    def github_user_repo(self) -> str:
        return self._repo.remotes.origin.url.split('.git')[0].split('/')[-2]

    @property
    def repo_name(self) -> str:
        return self._repo.remotes.origin.url.split('.git')[0].split('/')[-1]
