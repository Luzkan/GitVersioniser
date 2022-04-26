from dataclasses import dataclass

from git.repo import Repo


@dataclass
class Files:
    repo: Repo

    def add_all(self) -> None:
        self.repo.git.add("-A")
