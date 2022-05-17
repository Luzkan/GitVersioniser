from dataclasses import dataclass


@dataclass(frozen=True)
class CommitTag:
    full_name: str
    short_name: str
    emoji_representation: str
    patterns: list[str]

    def __str__(self):
        return self.patterns[0]
