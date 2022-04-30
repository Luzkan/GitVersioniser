<div align="center" style="margin-bottom: 30px;">
    <img src="./docs/img/logo.png" style="height: 128px; width; 128px;"/>
    <h2 align="center">GitVersioniser</h2>
    <div>
        <p style="font-style: italic;">Automatic Semantic Versioniser & Change Tracker [0.3.0+build.1]</p>
    </div>
</div>

# Hey! 😸

This repository contains a tool for automatic git repository versioning. It can be quickly introduced to any repository via Github Actions. If you ever felt too lazy to create individual tags for each change in your project, this tool will be handy.

# Table of Contents

1. [Features](#-features)
2. [Benefits](#-benefits)
3. [How can I run this?](#-how-can-i-run-this)
4. [How can I contribute?](#-how-can-i-contribute)
5. [Explore More!](#-explore-more)

---

## ✨ **Features**

- [Automatic Semantic Versioning](https://semver.org/) via Tags and prefixed Commit Messages.
- [Automatic Changelog Entries Creation](https://keepachangelog.com/en/1.0.0/) based on the Commit Messages
- Easily [adjustable](#-explore-more).
- Easily [extendible](#-how-can-i-contribute) by creating a new class that overrides just a single _abstract method_.

---

## 💰 **Benefits**

First and foremost - this tool will automatically create new semantic version tags for your repository. It will increment the build version by default, but you can choose what will get bumped using the [increment tags](./src/gitversioniser/config/increments.py). GitVersioniser will automatically add the version tag to the commit message in the default version, which gives an excellent overview of which files were when modified.

Using this repository out-of-the-box gives you a free, automatically managed `CHANGELOG.md` file. It uses [prefix tags](./src/gitversioniser/config/commit_tags.py) that are one-letter shorthands of the joint summarization of a commit. This will encourage the developers to create tiny and descriptive commits. Additionally, there will be no more fights over the usage of imperative _"Fix"_ or declarative _"Fixed"_. Everyone can add the rest individually in their thoughts to their liking.

_This repository is written to be understood as easily as reading documentation._

---

## 🚀 **How can I run this?**

Copy the [GitVersioniser.yml](./docs/example/GitVersioniser.yml) to the `.github/workflows/` in your repository!

---

## 🤔 **How can I contribute?**

If you would like to contribute, you are more than welcome by opening a new discussion on the [issues](https://github.com/Luzkan/gitversioniser/issues) or directly adding changes by opening new [merge requests](https://github.com/Luzkan/gitversioniser/pulls).

---

## 🔭 **Explore More!**

If you want to adjust the way of working to your liking, feel free to check the available options! Because we are the developers, I believe that the [documentation](https://luzkan.github.io/smells/what-comment) for us is just [duplicated code](https://luzkan.github.io/smells/duplicated-code). Thus, I encourage you to trust the [communicative](https://luzkan.github.io/smells/uncommunicative-name) [method names](https://luzkan.github.io/smells/fallacious-method-name) and see the options through code for yourself! 🐱

_Hint: Think about the repository as a device that can be entirely customized by the flavor-modules you choose to plug-in._

### [**Version**](./src/gitversioniser/domain/versioniser/routines/version/) based on:

- [Commits Till Last GitVersioniser Commit](./src/gitversioniser/domain/versioniser/routines/version/core/commits_till_last_gitversioniser_commit.py) _(default)_
- [Last Commit](./src/gitversioniser/domain/versioniser/routines/version/core/last_commit.py)

### [**Tagging**](./src/gitversioniser/domain/versioniser/routines/tagging/):

- [Always](./src/gitversioniser/domain/versioniser/routines/tagging/core/always.py) _(default)_
- [If Patch or Higher](./src/gitversioniser/domain/versioniser/routines/tagging/core/if_patch_or_higher.py)
- [If Prerelease or Higher](./src/gitversioniser/domain/versioniser/routines/tagging/core/if_prerelease_or_higher.py)
- [Null](./src/gitversioniser/domain/versioniser/routines/tagging/core/null.py)

### [**Commit Message**](./src/gitversioniser/domain/versioniser/routines/commit_message/):

- _[Prefix Version](./src/gitversioniser/domain/versioniser/routines/commit_message/core/prefix_version/):_
  - [Full](./src/gitversioniser/domain/versioniser/routines/commit_message/core/prefix_version/full.py) _(default)_
  - [Major Minor Patch](./src/gitversioniser/domain/versioniser/routines/commit_message/core/prefix_version/major_minor_patch.py)
  - [Major Minor Patch Prerelease](./src/gitversioniser/domain/versioniser/routines/commit_message/core/prefix_version/major_minor_patch_prerelease.py)
- _[Suffix Version](./src/gitversioniser/domain/versioniser/routines/commit_message/core/suffix_version/):_
  - [Full](./src/gitversioniser/domain/versioniser/routines/commit_message/core/suffix_version/full.py)
  - [Major Minor Patch](./src/gitversioniser/domain/versioniser/routines/commit_message/core/suffix_version/major_minor_patch.py)
  - [Major Minor Patch Prerelease](./src/gitversioniser/domain/versioniser/routines/commit_message/core/suffix_version/major_minor_patch_prerelease.py)
- [Null](./src/gitversioniser/domain/versioniser/routines/commit_message/core/null.py)

### [**Commiting**](./src/gitversioniser/domain/versioniser/routines/commiting/):

- [Push Main Amend](./src/gitversioniser/domain/versioniser/routines/commiting/core/push_main_amend.py) _(default)_
- [Push Main New](./src/gitversioniser/domain/versioniser/routines/commiting/core/push_main_new.py)

### [**File Updater**](./src/gitversioniser/domain/versioniser/routines/file_updater/):

- [Versionise Files](./src/gitversioniser/domain/versioniser/routines/file_updater/core/versionise_files.py) _(default)_
- [Null](./src/gitversioniser/domain/versioniser/routines/file_updater/core/null.py)

### [**Changelog**](./src/gitversioniser/domain/versioniser/routines/changelog/):

- [Commit Pattern](./src/gitversioniser/domain/versioniser/routines/changelog/core/commit_pattern/commit_pattern.py) _(default)_
- [Last Commit Message as Description](./src/gitversioniser/domain/versioniser/routines/changelog/core/last_commit_message_as_description/last_commit_message_as_description.py)
- [Null](./src/gitversioniser/domain/versioniser/routines/changelog/core/null/null.py)
