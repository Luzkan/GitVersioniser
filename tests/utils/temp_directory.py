from pathlib import Path


class TempDirectory:
    def __init__(self, directory_name: str = '../gitversioniser_test/'):
        self.directory_path = Path(directory_name)
        self.directory_path.mkdir(exist_ok=True)

    def __del__(self):
        """
        The directory can't be removed due to permission error on .git dir.
        Solution would be appreciated! :)
        """
        # shutil.rmtree(self.directory_path)
        pass
