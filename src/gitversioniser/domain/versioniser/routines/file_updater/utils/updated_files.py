from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class UpdatedFiles:
    paths: list[Path]

    @staticmethod
    def init_normalize(paths: list[Path | None]) -> 'UpdatedFiles':
        return UpdatedFiles([path for path in paths if path is not None])
