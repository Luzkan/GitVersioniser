from dataclasses import dataclass

from gitversioniser.helpers.version_bump import VersionBump


@dataclass
class Increment:
    pattern: str
    version_bump: VersionBump

    def __str__(self):
        return self.pattern
