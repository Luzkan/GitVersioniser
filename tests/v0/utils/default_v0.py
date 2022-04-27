import unittest
from unittest.mock import patch

from gitversioniser.config.arguments import Arguments
from gitversioniser.config.config import Config


class TestDefaultV0(unittest.TestCase):
    def get_config(self) -> Config:
        with patch('sys.argv', ['']) as _:
            arguments = Arguments.get_arguments()
            return Config(
                target_repository_path=self.test_repo_path,
                versioned_files=arguments.versioned_files,
                routines=arguments.routines,
            )

    def setUp(self):
        self.test_repo_path = '../gitversioniser_test/'
        self.config: Config = self.get_config()
