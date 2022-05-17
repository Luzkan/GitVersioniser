from parameterized import parameterized

from gitversioniser.config.routines.commit_message import CommitMessageArguments
from gitversioniser.domain.repository.semver_tag import SemverTag
from tests.v0.routines.commit_message.routine import TestRoutineCommitMessage


class TestEmojiVersionPrefix(TestRoutineCommitMessage):
    def setUp(self):
        super().setUp()
        self.routine = self.get_routine(CommitMessageArguments(
            describe_changes='WithEmoji',
            format_version_tag='FullButOnlyDigits',
            place_version_tag='Prefix',
            summarize_changes='WithEmojiCounted'
        ))

    @parameterized.expand([
        (
            SemverTag.init_spec(1, 0, 0),
            (
                'Summary of smth\n'
                '\n'
                'F: Bugged Foo\n'
                'R: Width of Boo\n'
                '\n'
                'ISSUE: 342'
            ),
            (
                '[`1.0.0`] 🛠️🗑️ Summary of smth\n'
                '\n'
                '🛠️ Bugged Foo\n'
                '🗑️ Width of Boo\n'
                '\n'
                'ISSUE: 342'
            ),
        ),
        (
            SemverTag.init_spec(2, 4, 6, 'rc.3', 'build.4'),
            (
                'The requested Foo Thing for Boo\n'
                '\n'
                'F: Bugged Foo\n'
                'C: Looks of Foo\n'
                'F: Glitched Foo\n'
                'R: Width of Boo\n'
                '\n'
                'ISSUE: 342'
            ),
            (
                '[`2.4.6-3+4`] 🛠️²🔸🗑️ The requested Foo Thing for Boo\n'
                '\n'
                '🛠️ Bugged Foo\n'
                '🔸 Looks of Foo\n'
                '🛠️ Glitched Foo\n'
                '🗑️ Width of Boo\n'
                '\n'
                'ISSUE: 342'
            ),
        ),
        (
            SemverTag.init_spec(1, 0, 0),
            (
                'A: Just the changes\n'
                'C: No Summary\n'
                'C: No Description\n'
                'D: No Footer\n'
            ),
            (
                '[`1.0.0`] ✨🔸²🔚 Just the changes\n'
                '\n'
                '✨ Just the changes\n'
                '🔸 No Summary\n'
                '🔸 No Description\n'
                '🔚 No Footer'
            ),
        ),
        (
            SemverTag.init_spec(2, 0, 0),
            (
                'This is a merge request.\n'
                '\n'
                '* C: No Summary\n'
                '\n'
                'I wanted to greet everyone in my last commit of MR.\n'
                '\n'
                '* A: Second Requested Feature.\n'
                '\n'
                '* A: First Requested Feature. No footer in this MR Commit Message.\n'
            ),
            (
                '[`2.0.0`] 🔸✨² This is a merge request.\n'
                '\n'
                '🔸 No Summary\n'
                '✨ Second Requested Feature.\n'
                '✨ First Requested Feature. No footer in this MR Commit Message.\n'
                '\n'
                'I wanted to greet everyone in my last commit of MR.'
            ),
        ),
        (
            SemverTag.init_spec(2, 0, 0),
            (
                'This is a merge request.\n'
                '\n'
                '* C: Did something\n'
                '\n'
                'I wanted to greet everyone in my last commit of MR.\n'
                '\n'
                '* C: Second Requested Feature.\n'
                '\n'
                'Describing a little bit more about second feature.\n'
                'And so I described it\n'
                '\n'
                'ID: 232\n'
                '\n'
                '* A: First Requested Feature. No footer in this MR Commit Message.\n'
                '\n'
                'This is a major thing, check documentation!\n'
                '\n'
                'ID: 231\n'
            ),
            (
                '[`2.0.0`] 🔸²✨ This is a merge request.\n'
                '\n'
                '🔸 Did something\n'
                '🔸 Second Requested Feature.\n'
                '✨ First Requested Feature. No footer in this MR Commit Message.\n'
                '\n'
                'I wanted to greet everyone in my last commit of MR.\n'
                '\n'
                '\n'
                'Describing a little bit more about second feature.\n'
                'And so I described it\n'
                '\n'
                'ID: 232\n'
                '\n'
                '\n'
                'This is a major thing, check documentation!\n'
                '\n'
                'ID: 231'
            ),
        ),
        (
            SemverTag.init_spec(2, 0, 0, 'rc.1', 'build.420'),
            (
                'F: This has no summary and footer\n'
            ),
            (
                '[`2.0.0-1+420`] 🛠️ This has no summary and footer'
            ),
        ),
        (
            SemverTag.init_spec(2, 0, 0, 'rc.1', 'build.420'),
            (
                'F: This has no summary but has a description/footer\n'
                '\n'
                'I am a description/footer\n'
            ),
            (
                '[`2.0.0-1+420`] 🛠️ This has no summary but has a description/footer\n'
                '\n'
                'I am a description/footer'
            ),
        ),
        (
            SemverTag.init_spec(1, 2, 3, 'build.4'),
            (
                'This has no tag at all\n'
            ),
            (
                '[`1.2.3-4`] This has no tag at all'
            ),
        ),
        (
            SemverTag.init_spec(1, 1, 0, 'rc.1'),
            (
                'This has a summary\n'
                '\n'
                'And a footer\n'
            ),
            (
                '[`1.1.0-1`] This has a summary\n'
                '\n'
                'And a footer'
            ),
        ),
    ])
    def test_true(self, version_info, commit_message, expected_commit_message):
        self.routine.repo.commits.commit(commit_message)
        print(
            '\n\n'
            '---Generated---\n'
            f"{self.routine.run(version_info).new}\n"
            f"---Expected---\n"
            f"{expected_commit_message}\n"
            '-----\n\n'
        )
        self.assertEqual(str(self.routine.run(version_info).new), expected_commit_message)
