from dataclasses import dataclass


@dataclass(frozen=True)
class Credentials:
    username: str = "GitVersioniser"
    email: str = "luzkan.gitversioniser@github.com"
