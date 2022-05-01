from parameterized import parameterized
from semver import VersionInfo

from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.version.routine import TestRoutineVersion


class TestLastCommit(TestRoutineVersion):

    def perform_version_test(self, old_version, last_commit_message, new_version):
        self.routine.repo.tags.create(str(old_version))
        self.routine.repo.commits.commit(str(last_commit_message))
        versions: Versions = self.routine.run()
        self.assertEqual(versions.old, self.routine.repo.tags.latest_semver)
        self.assertEqual(versions.new, new_version)

    @parameterized.expand([
        (VersionInfo(1, 2, 3), 'A: New Feature', VersionInfo(1, 2, 3, build='build.1')),
        (VersionInfo(1, 2, 3, build='build.2'), 'R: Feature', VersionInfo(1, 2, 3, build='build.3')),
        (VersionInfo(1, 2, 3, 'rc.2'), 'C: Thing', VersionInfo(1, 2, 3, 'rc.2', build='build.1')),
        (VersionInfo(1, 2, 3, 'rc.4'), 'F: Thing \n Yey', VersionInfo(1, 2, 3, 'rc.4', build='build.1')),
    ])
    def test_no_specifier(self, old_version, last_commit_message, new_version):
        self.perform_version_test(old_version, last_commit_message, new_version)

    @parameterized.expand([
        (VersionInfo(1, 2, 3), 'A: New Feature #major', VersionInfo(2, 0, 0)),
        (VersionInfo(1, 2, 3, build='build.2'), 'R: #major Feature', VersionInfo(2, 0, 0)),
        (VersionInfo(1, 2, 3, 'rc.2'), '#major C: Thing', VersionInfo(2, 0, 0)),
        (VersionInfo(1, 2, 3, 'rc.4'), 'F: Things \n Yey #major', VersionInfo(2, 0, 0)),
    ])
    def test_major_specifier(self, old_version, last_commit_message, new_version):
        self.perform_version_test(old_version, last_commit_message, new_version)

    @parameterized.expand([
        (VersionInfo(1, 2, 3), 'A: New Feature #minor', VersionInfo(1, 3, 0)),
        (VersionInfo(1, 2, 3, build='build.2'), 'R: #minor Feature', VersionInfo(1, 3, 0)),
        (VersionInfo(1, 2, 3, 'rc.2'), '#minor C: Thing', VersionInfo(1, 3, 0)),
        (VersionInfo(1, 2, 3, 'rc.4'), 'F: Things \n Yey #minor', VersionInfo(1, 3, 0)),
    ])
    def test_minor_specifier(self, old_version, last_commit_message, new_version):
        self.perform_version_test(old_version, last_commit_message, new_version)

    @parameterized.expand([
        (VersionInfo(1, 2, 3), 'A: New Feature #patch', VersionInfo(1, 2, 4)),
        (VersionInfo(1, 2, 3, build='build.2'), 'R: #patch Feature', VersionInfo(1, 2, 4)),
        (VersionInfo(1, 2, 3, 'rc.2'), '#patch C: Thing', VersionInfo(1, 2, 4)),
        (VersionInfo(1, 2, 3, 'rc.4'), 'F: Things \n Yey #patch', VersionInfo(1, 2, 4)),
    ])
    def test_patch_specifier(self, old_version, last_commit_message, new_version):
        self.perform_version_test(old_version, last_commit_message, new_version)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('last_commit')
        self.repo_utils = PseudoRepo(self.routine)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
