from parameterized import parameterized

from gitversioniser.domain.repository.semver_tag import SemverTag
from gitversioniser.domain.versioniser.utils.versions import Versions
from tests.utils.pseudo_repo import PseudoRepo
from tests.v0.routines.version.routine import TestRoutineVersion


class TestVersionTagInLastCommit(TestRoutineVersion):
    @parameterized.expand([
        (
            SemverTag.init_spec(1, 2, 3),
            'A: New Feature',
            SemverTag.init_spec(1, 2, 4, 'alpha.1')
        ),
        (
            SemverTag.init_spec(1, 2, 3, build='build.2'),
            'R: Feature',
            SemverTag.init_spec(1, 2, 3, build='build.3')
        ),
        (
            SemverTag.init_spec(1, 2, 3, 'rc.2'),
            'C: Thing',
            SemverTag.init_spec(1, 2, 3, 'rc.2', build='build.1')
        ),
        (
            SemverTag.init_spec(1, 2, 3, 'rc.4'),
            'F: Thing \n Yey',
            SemverTag.init_spec(1, 2, 3, 'rc.4', build='build.1')
        ),
    ])
    def test_no_specifier(self, old_version, last_commit_message, new_version):
        self.start_test(old_version, last_commit_message, new_version)

    @parameterized.expand([
        (
            SemverTag.init_spec(1, 2, 3),
            'A: New Feature #major',
            SemverTag.init_spec(2, 0, 0)),
        (
            SemverTag.init_spec(1, 2, 3, build='build.2'),
            'R: #major Feature',
            SemverTag.init_spec(2, 0, 0)),
        (
            SemverTag.init_spec(1, 2, 3, 'rc.2'),
            '#major C: Thing',
            SemverTag.init_spec(2, 0, 0)),
        (
            SemverTag.init_spec(1, 2, 3, 'rc.4'),
            'F: Things \n Yey #major',
            SemverTag.init_spec(2, 0, 0)),
    ])
    def test_major_specifier(self, old_version, last_commit_message, new_version):
        self.start_test(old_version, last_commit_message, new_version)

    @parameterized.expand([
        (
            SemverTag.init_spec(1, 2, 3),
            'A: New Feature #minor',
            SemverTag.init_spec(1, 3, 0)
        ),
        (
            SemverTag.init_spec(1, 2, 3, build='build.2'),
            'R: #minor Feature',
            SemverTag.init_spec(1, 3, 0)
        ),
        (
            SemverTag.init_spec(1, 2, 3, 'rc.2'),
            '#minor C: Thing',
            SemverTag.init_spec(1, 3, 0)
        ),
        (
            SemverTag.init_spec(1, 2, 3, 'rc.4'),
            'F: Things \n Yey #minor',
            SemverTag.init_spec(1, 3, 0)
        ),
    ])
    def test_minor_specifier(self, old_version, last_commit_message, new_version):
        self.start_test(old_version, last_commit_message, new_version)

    @parameterized.expand([
        (
            SemverTag.init_spec(1, 2, 3),
            'A: New Feature #patch',
            SemverTag.init_spec(1, 2, 4)
        ),
        (
            SemverTag.init_spec(1, 2, 3, build='build.2'),
            'R: #patch Feature',
            SemverTag.init_spec(1, 2, 4)
        ),
        (
            SemverTag.init_spec(1, 2, 3, 'rc.2'),
            '#patch C: Thing',
            SemverTag.init_spec(1, 2, 4)
        ),
        (
            SemverTag.init_spec(1, 2, 3, 'rc.4'),
            'F: Things \n Yey #patch',
            SemverTag.init_spec(1, 2, 4)
        ),
    ])
    def test_patch_specifier(self, old_version, last_commit_message, new_version):
        self.start_test(old_version, last_commit_message, new_version)

    def start_test(self, old_version, last_commit_message, new_version):
        self.routine.repo.tags.create(str(old_version))
        self.routine.repo.commits.commit(str(last_commit_message))
        versions: Versions = self.routine.run()
        self.assertEqual(versions.old, self.routine.repo.tags.latest_semver)
        self.assertEqual(versions.new, new_version)

    def setUp(self):
        super().setUp()
        self.routine = self.get_routine('VersionTagInLastCommit')
        self.repo_utils = PseudoRepo(self.routine.config, self.routine.repo)

    def tearDown(self):
        self.repo_utils.delete_all_tags()
