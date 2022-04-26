from dataclasses import dataclass


@dataclass
class Credentials:
    username: str = "GitVersioniser"
    email: str = "git@versioniser.com"
