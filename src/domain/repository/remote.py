from dataclasses import dataclass

from git.repo import Repo


@dataclass
class Remote:
    repo: Repo

    def raise_if_changes(self):
        if self.repo.git.pull("--ff-only").strip() != "Already up to date.":
            raise RuntimeError("There are new changes in the repository.")

    def create_tag(self, version: str):
        return self.repo.create_tag(version)

    def push(self):
        return self.repo.remote("origin").push()

    def push_force(self):
        return self.repo.remote("origin").push(force=True)

    def push_tags(self):
        return self.repo.remote("origin").push(tags=True)
