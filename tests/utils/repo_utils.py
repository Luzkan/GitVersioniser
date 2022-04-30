from dataclasses import dataclass

from gitversioniser.domain.versioniser.routines.abstract import Routine


@dataclass
class RepoUtils:
    routine: Routine

    def create_commits(self, commit_messages: list[str]) -> None:
        for commit_message in commit_messages:
            self.routine.repo._repo.git.commit("--allow-empty", "-m", commit_message, "--author=Bob <bob@github.com>")

    def create_gitversioniser_commit(self, commit_message: str):
        gitversioniser_author: str = f"--author={self.routine.config.credentials.username} <{self.routine.config.credentials.email}>"
        self.routine.repo._repo.git.commit("--allow-empty", "-m", commit_message, gitversioniser_author)

    def create_remote(self):
        self.routine.repo._repo.create_remote('origin', 'https://github.com/Luzkan/GitVersioniserTest.git')

    def delete_remote(self, name: str = 'origin') -> None:
        try:
            self.routine.repo._repo.delete_remote(self.routine.repo._repo.remote(name))
        except ValueError:
            pass

    def delete_all_tags(self) -> None:
        for tag in self.routine.repo.tags.get_sorted:
            self.routine.repo._repo.git.tag('-d', tag)
