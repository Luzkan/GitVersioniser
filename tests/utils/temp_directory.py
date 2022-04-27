from pathlib import Path


class TempDirectory:
    def __init__(self, directory_name: str = '../gitversioniser_test/'):
        self.directory_path = Path(directory_name)
        self.directory_path.mkdir(exist_ok=True)

    def __enter__(self):
        return self.directory_path

    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):
        # TODO, figure to remove the directory after test is done
        # shutil.rmtree(self.directory_path)
        pass
