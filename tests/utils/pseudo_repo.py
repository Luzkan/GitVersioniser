from dataclasses import dataclass

from gitversioniser.config.config import Config
from gitversioniser.domain.repository.git_repository import GitRepository


@dataclass
class PseudoRepo:
    config: Config
    repo: GitRepository

    def create_commits(self, commit_messages: list[str]) -> None:
        for commit_message in commit_messages:
            self.repo._repo.git.commit("--allow-empty", "-m", commit_message, "--author=Bob <bob@github.com>")

    def create_gitversioniser_commit(self, commit_message: str):
        gitversioniser_author: str = f"--author={self.config.credentials.username} <{self.config.credentials.email}>"
        self.repo._repo.git.commit("--allow-empty", "-m", commit_message, gitversioniser_author)

    def create_remote(self):
        self.repo._repo.create_remote('origin', 'https://github.com/Luzkan/GitVersioniserTest.git')

    def delete_remote(self, name: str = 'origin') -> None:
        try:
            self.repo._repo.delete_remote(self.repo._repo.remote(name))
        except ValueError:
            pass

    def delete_all_tags(self) -> None:
        for tag in self.repo.tags.get_sorted:
            self.repo._repo.git.tag('-d', tag)
