from semver import VersionInfo

from tests.utils.temp_directory import TempDirectory
from tests.v0.routines.utils.routine import TestRoutine


class TestCommitTag(TestRoutine):
    def test_default_arguments_main(self):
        with TempDirectory(self.test_repo_path) as _:
            self.routine = self.get_routine('prefix_tag')
            self.routine.target_repo.commits.commit('Initial Commit')
            self.assertEqual(self.routine.run(VersionInfo(1, 0, 0)), '[`1.0.0`] Initial Commit')
