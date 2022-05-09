import unittest
from unittest.mock import patch

from git.repo import Repo
from hypothesis import settings

from gitversioniser.config.arguments import Arguments
from gitversioniser.config.config import Config
from gitversioniser.domain.repository.git_repository import GitRepository


class TestGeneralScenario(unittest.TestCase):
    def get_config(self) -> Config:
        with patch('sys.argv', ['']) as _:
            arguments = Arguments.get_arguments()
            return Config(
                target_repository_path=self.test_repo_path,
                versioned_files=arguments.versioned_files,
                routines=arguments.routines,
                patterns=arguments.patterns,
            )

    def setUp(self):
        settings(deadline=None, max_examples=50)
        self.test_repo_path = '../gitversioniser_test/'
        self.config: Config = self.get_config()
        self.repo = GitRepository(self.config, _repo=Repo(self.config.target_repository_path))
