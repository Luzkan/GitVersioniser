<div align="center" style="margin-bottom: 30px;">
    <img src="./img/logo.png" style="height: 128px; width; 128px;"/>
    <h2 align="center"><a href="https://github.com/Luzkan/GitVersioniser">GitVersioniser</a></h2>
    <div>
        <i>Automatic Semantic Versioniser & Change Tracker</code></i>
    </div>
</div>

---

## 🔭 **Explore More!**

If you want to adjust the way of working to your liking, feel free to check the available options! Because we are the developers, I believe that the [documentation](https://luzkan.github.io/smells/what-comment) for us is just [duplicated code](https://luzkan.github.io/smells/duplicated-code). Thus, I encourage you to trust the [communicative](https://luzkan.github.io/smells/uncommunicative-name) [method names](https://luzkan.github.io/smells/fallacious-method-name) and see the options through code for yourself! 🐱

_Hint: Think about the repository as a device that can be entirely customized by the flavor-modules you choose to plug-in. Simply copy the class name and replace it in [yml config](../docs/example/GitVersioniser.yml)._

### [**Version**](../src/gitversioniser/domain/versioniser/routines/version/) based on:

- [Version Tag In Commits Till Last GitVersioniser Commit](../src/gitversioniser/domain/versioniser/routines/version/core/version_tag_in_commits_till_last_git_versioniser_commit.py) _(default)_
- [Version Tag In Last Commit](../src/gitversioniser/domain/versioniser/routines/version/core/version_tag_in_last_commit.py)

### [**Should Contribute**](../src/gitversioniser/domain/versioniser/routines/version/) when:

- [If a New Version Is Build or Higher](../src/gitversioniser/domain/versioniser/routines/should_contribute/core/if_new_version_is_build_or_higher.py) _(default)_
- [If a New Version Is Pre-Release or Higher](../src/gitversioniser/domain/versioniser/routines/should_contribute/core/if_new_version_is_prerelease_or_higher.py)
- [If a New Version Is Patch or Higher](../src/gitversioniser/domain/versioniser/routines/should_contribute/core/if_new_version_is_patch_or_higher.py)
- [Never](../src/gitversioniser/domain/versioniser/routines/should_contribute/core/never.py)

### [**Tagging**](../src/gitversioniser/domain/versioniser/routines/tagging/):

- [Regular](../src/gitversioniser/domain/versioniser/routines/tagging/core/regular.py) _(default)_
- [Force](../src/gitversioniser/domain/versioniser/routines/tagging/core/force.py)
- [Never](../src/gitversioniser/domain/versioniser/routines/tagging/core/never.py)

### [**Prefix Tag with '`v`'**](../src/gitversioniser/domain/versioniser/routines/tagging/):

- [Always](../src/gitversioniser/domain/versioniser/routines/prefix_tag_with_v/core/always.py) _(default)_
- [If a New Version is Build or Higher](../src/gitversioniser/domain/versioniser/routines/prefix_tag_with_v/core/if_new_version_is_build_or_higher.py)
- [If a New Version is Pre-Release or Higher](../src/gitversioniser/domain/versioniser/routines/prefix_tag_with_v/core/if_new_version_is_prerelease_or_higher.py)
- [If a New Version is Patch or Higher](../src/gitversioniser/domain/versioniser/routines/prefix_tag_with_v/core/if_new_version_is_patch_or_higher.py)
- [Never](../src/gitversioniser/domain/versioniser/routines/prefix_tag_with_v/core/never.py)

### [**Commit Message**](../src/gitversioniser/domain/versioniser/routines/commit_message/):

- _[**Describe Changes**](../src/gitversioniser/domain/versioniser/routines/commit_message/describe_changes/)_:
  - [With Emoji](../src/gitversioniser/domain/versioniser/routines/commit_message/describe_changes/with_emoji.py) _(default)_
  - [With Letters](../src/gitversioniser/domain/versioniser/routines/commit_message/describe_changes/with_letters.py)
  - [Null](../src/gitversioniser/domain/versioniser/routines/commit_message/describe_changes/null.py)
- _[**Format Version Tag**](../src/gitversioniser/domain/versioniser/routines/commit_message/format_version_tag/)_:
  - [Full](../src/gitversioniser/domain/versioniser/routines/commit_message/format_version_tag/full.py)
  - [Full But Only Digits](../src/gitversioniser/domain/versioniser/routines/commit_message/format_version_tag/full_but_only_digits.py) _(default)_
  - [Major Minor Patch](../src/gitversioniser/domain/versioniser/routines/commit_message/format_version_tag/major_minor_patch.py)
  - [Major Minor Patch Pre-Release](../src/gitversioniser/domain/versioniser/routines/commit_message/format_version_tag/major_minor_patch_prerelease.py)
- _[**Place Version Tag**](../src/gitversioniser/domain/versioniser/routines/commit_message/place_version_tag/)_:
  - [Prefix](../src/gitversioniser/domain/versioniser/routines/commit_message/place_version_tag/prefix.py) _(default)_
  - [Suffix](../src/gitversioniser/domain/versioniser/routines/commit_message/place_version_tag/suffix.py)
  - [Null](../src/gitversioniser/domain/versioniser/routines/commit_message/place_version_tag/null.py)
- _[**Summarize Changes**](../src/gitversioniser/domain/versioniser/routines/commit_message/summarize_changes/)_:
  - [With Emoji Counted](../src/gitversioniser/domain/versioniser/routines/commit_message/summarize_changes/with_emoji_counted.py) _(default)_
  - [With Emoji Symbolic](../src/gitversioniser/domain/versioniser/routines/commit_message/summarize_changes/with_emoji_symbolic.py)
  - [With Letters](../src/gitversioniser/domain/versioniser/routines/commit_message/summarize_changes/with_letters.py)
  - [Null](../src/gitversioniser/domain/versioniser/routines/commit_message/summarize_changes/null.py)

### [**Commiting**](../src/gitversioniser/domain/versioniser/routines/commiting/):

- [Push Origin Amend](../src/gitversioniser/domain/versioniser/routines/commiting/core/push_origin_amend.py) _(default)_
- [Push Origin New Commit](../src/gitversioniser/domain/versioniser/routines/commiting/core/push_origin_new_commit.py)

### [**File Updater**](../src/gitversioniser/domain/versioniser/routines/file_updater/):

- [Versionise Files](../src/gitversioniser/domain/versioniser/routines/file_updater/core/versionise_files.py) _(default)_
- [Null](../src/gitversioniser/domain/versioniser/routines/file_updater/core/null.py)

### [**Changelog**](../src/gitversioniser/domain/versioniser/routines/changelog/) based on:

- [Commit Changelog Tags](../src/gitversioniser/domain/versioniser/routines/changelog/core/commit_change_tags/commit_change_tags.py) _(default)_
- [Last Commit Message as Description](../src/gitversioniser/domain/versioniser/routines/changelog/core/last_commit_message_as_description/last_commit_message_as_description.py)
- [Null](../src/gitversioniser/domain/versioniser/routines/changelog/core/null/null.py)
