from dataclasses import dataclass
from pathlib import Path


@dataclass
class Utils:
    testing_repo: Path

    def check_tag(self, path: Path):
        pass
