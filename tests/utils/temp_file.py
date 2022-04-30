from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class TempFile:
    filepath: Path = field(init=False)

    def open(self, path: Path):
        with path.open('r') as file:
            return file.read()

    def remove(self):
        if self.filepath and self.filepath.exists():
            self.filepath.unlink()

    def prepare_environment(self, path: Path, content: str) -> Path:
        def create_file(path: Path):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
            self.filepath = path

        def write_to_file(path: Path, content: str):
            with path.open('w') as file:
                file.write(content)

        create_file(path)
        write_to_file(path, content)
        return path
