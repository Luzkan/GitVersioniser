from dataclasses import dataclass, field

from git.repo import Repo

from config.config import Config
from domain.repository.commits import Commits
from domain.repository.files import Files
from domain.repository.remote import Remote
from domain.repository.tags import Tags


@dataclass
class GitRepository:
    config: Config
    repo: Repo = field(default=Repo())
    files: Files = field(init=False)
    remote: Remote = field(init=False)
    tags: Tags = field(init=False)
    commits: Commits = field(init=False)

    def __post_init__(self):
        def init_submodules():
            self.files = Files(self.repo)
            self.remote = Remote(self.repo)
            self.tags = Tags(self.repo)
            self.commits = Commits(self.config, self.repo)

        init_submodules()

    @property
    def github_user_repo(self) -> str:
        return self.repo.remotes.origin.url.split('.git')[0].split('/')[-2]

    @property
    def repo_name(self) -> str:
        return self.repo.remotes.origin.url.split('.git')[0].split('/')[-1]
