from dataclasses import dataclass

from git.repo import Repo

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.commit import Commit


@dataclass
class Commits:
    config: Config
    repo: Repo

    @property
    def latest(self) -> Commit:
        return Commit(self.config, _commit=self.repo.commit())

    def commit(self, message: str):
        self.repo.git.commit("--allow-empty", "-m", message)

    def commit_amend(self, message: str):
        self.repo.git.commit("--allow-empty", "--amend", "-m", message)

    def get_commits_till_last_commit_made_by_author(self, author: str) -> list[Commit]:
        """ Returned list of commits is in descending date order. """
        def recursivelly_check(current_commits: tuple[Commit], acc: list[Commit]):
            for current_commit in reversed(current_commits):
                if current_commit.is_made_by_author(author) or current_commit.get_parents_count <= 1:
                    return acc
                return recursivelly_check(current_commit.get_parents(), [current_commit] + acc)
        return recursivelly_check((self.latest,), list())
