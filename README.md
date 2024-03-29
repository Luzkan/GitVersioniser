<div align="center" style="margin-bottom: 30px;">
    <img src="./docs/img/logo.png" style="height: 128px; width; 128px;"/>
    <h2 align="center">GitVersioniser</h2>
    <div>
        <i>Automatic Semantic Versioniser & Change Tracker <code>[0.6.1]</code></i>
    </div>
</div>

# Hey! 😸

This repository contains a tool for automatic git repository versioning. It can be quickly introduced to any repository via Github Actions. If you ever felt too lazy to create individual tags for each change in your project, this tool will be handy.

# Table of Contents

1. [Features](#-features)
2. [How can I run this?](#-how-can-i-run-this)
3. [How can I use this?](#-how-can-i-use-this)
4. [How can I contribute?](#-how-can-i-contribute)
5. [Benefits](#-benefits)
6. [Explore More!](#-explore-more)

---

## ✨ **Features**

- [Automatic Semantic Versioning](https://semver.org/) via Tags, File Modifications and Commit Messages.
- [Automatic Changelog Entries Creation](https://keepachangelog.com/en/1.0.0/) based on the Commit Messages.
- Easily [adjustable](#-explore-more).
- Easily [extendible](#-how-can-i-contribute) by creating a new class that overrides just a single _abstract method_.

---

## 🚀 **How can I run this?**

Copy the [GitVersioniser.yml](./docs/example/GitVersioniser.yml) to the `.github/workflows/` in your repository!

---

## 🙌 **How can I use this?**

- You can start start any line in message with `A:` _(added)_, `F:` _(fixed)_, `R:` _(removed)_, ... etc., to [tag](./src/gitversioniser/config/patterns/commit_change_tags/changelog_category.py) the action you did, which will create corresponding changelog entry.
- You can add `#major`, `#minor`, `#patch`, ... etc., to [increment](./src/gitversioniser/config/patterns/commit_increment_tags/core/hashtag_explicit.py) version of the repository.
src\gitversioniser\config\patterns\commit_change_tags\changelog_category.py
---

## 🤔 **How can I contribute?**

If you would like to contribute, you are more than welcome by opening a new discussion on the [issues](https://github.com/Luzkan/gitversioniser/issues) or directly adding changes by opening new [merge requests](https://github.com/Luzkan/gitversioniser/pulls).

---

## 💰 **Benefits**

First and foremost - this tool will automatically create new semantic version tags for your repository. It will increment the build version by default, but you can choose what will get bumped using the [increment tags](./src/gitversioniser/config/patterns/commit_increment_tags/core/hashtag_explicit.py). GitVersioniser will automatically add the version tag to the commit message in the default version, which gives an excellent overview of which files were when modified.

Using this repository out-of-the-box gives you a free, automatically managed `CHANGELOG.md` file. It uses [prefix tags](./src/gitversioniser/config/commit_change_tags/core/classic_changelog.py) that are one-letter shorthands of the joint summarization of a commit. This will encourage the developers to create tiny and descriptive commits. Additionally, there will be no more fights over the usage of imperative _"Fix"_ or declarative _"Fixed"_. Everyone can add the rest individually in their thoughts to their liking.

_This repository is written to be understood as easily as reading documentation._

---

## 🔭 **Explore More!**

If you want to adjust the way of working to your liking, feel free to check the available options! Because we are the developers, I believe that the [documentation](https://luzkan.github.io/smells/what-comment) for us is just [duplicated code](https://luzkan.github.io/smells/duplicated-code). Thus, I encourage you to trust the [communicative](https://luzkan.github.io/smells/uncommunicative-name) [method names](https://luzkan.github.io/smells/fallacious-method-name) and see the options through code for yourself! 🐱

_Hint: Think about the repository as a device that can be entirely customized by the flavor-modules you choose to plug-in. Simply copy the class name and replace it in [yml config](./docs/example/GitVersioniser.yml)._

### [**Version**](./src/gitversioniser/domain/versioniser/routines/version/core/) based on:

- [Version Tag In Commits Till Last GitVersioniser Commit](./src/gitversioniser/domain/versioniser/routines/version/core/version_tag_in_commits_till_last_git_versioniser_commit.py) _(default)_
- [Version Tag In Last Commit](./src/gitversioniser/domain/versioniser/routines/version/core/version_tag_in_last_commit.py)

### [**Tagging**](./src/gitversioniser/domain/versioniser/routines/tagging/core/):

- [Regular](./src/gitversioniser/domain/versioniser/routines/tagging/core/regular.py) _(default)_
- [Force](./src/gitversioniser/domain/versioniser/routines/tagging/core/force.py)

### [**Prefix Tag with '`v`'**](./src/gitversioniser/domain/versioniser/routines/tagging/core/):

- [Always](./src/gitversioniser/domain/versioniser/routines/prefix_tag_with_v/core/always.py) _(default)_
- [Never](./src/gitversioniser/domain/versioniser/routines/prefix_tag_with_v/core/never.py)

### [**Commit Message**](./src/gitversioniser/domain/versioniser/routines/commit_message/):

- _[**Describe Changes**](./src/gitversioniser/domain/versioniser/routines/commit_message/describe_changes/)_:
  - [With Emoji](./src/gitversioniser/domain/versioniser/routines/commit_message/describe_changes/with_emoji.py) _(default)_
  - [With Letters](./src/gitversioniser/domain/versioniser/routines/commit_message/describe_changes/with_letters.py)
  - [Null](./src/gitversioniser/domain/versioniser/routines/commit_message/describe_changes/null.py)
- _[**Format Version Tag**](./src/gitversioniser/domain/versioniser/routines/commit_message/format_version_tag/)_:
  - [Full](./src/gitversioniser/domain/versioniser/routines/commit_message/format_version_tag/full.py)
  - [Full But Only Digits](./src/gitversioniser/domain/versioniser/routines/commit_message/format_version_tag/full_but_only_digits.py) _(default)_
  - [Major Minor Patch](./src/gitversioniser/domain/versioniser/routines/commit_message/format_version_tag/major_minor_patch.py)
  - [Major Minor Patch Pre-Release](./src/gitversioniser/domain/versioniser/routines/commit_message/format_version_tag/major_minor_patch_prerelease.py)
- _[**Place Version Tag**](./src/gitversioniser/domain/versioniser/routines/commit_message/place_version_tag/)_:
  - [Prefix](./src/gitversioniser/domain/versioniser/routines/commit_message/place_version_tag/prefix.py) _(default)_
  - [Suffix](./src/gitversioniser/domain/versioniser/routines/commit_message/place_version_tag/suffix.py)
  - [Null](./src/gitversioniser/domain/versioniser/routines/commit_message/place_version_tag/null.py)
- _[**Summarize Changes**](./src/gitversioniser/domain/versioniser/routines/commit_message/summarize_changes/)_:
  - [With Emoji Counted](./src/gitversioniser/domain/versioniser/routines/commit_message/summarize_changes/with_emoji_counted.py) _(default)_
  - [With Emoji Symbolic](./src/gitversioniser/domain/versioniser/routines/commit_message/summarize_changes/with_emoji_symbolic.py)
  - [With Letters](./src/gitversioniser/domain/versioniser/routines/commit_message/summarize_changes/with_letters.py)
  - [Null](./src/gitversioniser/domain/versioniser/routines/commit_message/summarize_changes/null.py)

### [**Commiting**](./src/gitversioniser/domain/versioniser/routines/commiting/core/):

- [Push Origin Amend](./src/gitversioniser/domain/versioniser/routines/commiting/core/push_origin_amend.py) _(default)_
- [Push Origin New Commit](./src/gitversioniser/domain/versioniser/routines/commiting/core/push_origin_new_commit.py)

### [**File Updater**](./src/gitversioniser/domain/versioniser/routines/file_updater/core/):

- [Versionise Files](./src/gitversioniser/domain/versioniser/routines/file_updater/core/versionise_files.py) _(default)_
- [Null](./src/gitversioniser/domain/versioniser/routines/file_updater/core/null.py)

### [**Changelog**](./src/gitversioniser/domain/versioniser/routines/changelog/core/) based on:

- [Commit Changelog Tags](./src/gitversioniser/domain/versioniser/routines/changelog/core/commit_change_tags/commit_change_tags.py) _(default)_
- [Last Commit Message as Description](./src/gitversioniser/domain/versioniser/routines/changelog/core/last_commit_message_as_description/last_commit_message_as_description.py)
- [Null](./src/gitversioniser/domain/versioniser/routines/changelog/core/null/null.py)

_For more available options, check out the [`FEATURES.md`](./docs/FEATURES.md) file!_
