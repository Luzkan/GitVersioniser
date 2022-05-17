# Changelog

[Git Versioniser](https://github.com/Luzkan/GitVersioniser) automatically versions this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

_Note: New changelog entries are going to be created after the first horizontal line._

---

## [[`0.5.3+build.3`]] - 2022-05-17

### Added

- Commit Changes can be represented with emojis



## [[`0.5.3+build.2`]] - 2022-05-11

### Refactorization

- Summary in Commit Message is now string instead of a class

### Removed

- @property shortcut to summary and description in commit

### CI

- Updated configuration to use extended tags



## [[`0.5.3+build.1`]] - 2022-05-11

### Changed

- Config Structure - Patterns



## [[`0.5.3`]] - 2022-05-11

### Added

- Emoji Representation of Commit Change Tags

### Changed

- "Commit Changelog Tag name" to "Commit Change Tag"



## [[`0.5.2`]] - 2022-05-11

### Changed

- Commit Tag Pattern now is checked via regex #patch



## [[`0.5.1`]] - 2022-05-09

### Added

- Abstraction on Commit Tags (Changelog & Increment)



## [[`0.5.0+build.2`]] - 2022-05-06

### Changed

- Injecting Dependencies to RoutineManager



## [[`0.5.0+build.1`]] - 2022-05-06

### Changed

- Frozen Configuration (made them immutable)



## [[`0.5.0`]] - 2022-05-04

### Changed

- Routine Configuration is now Class name based (thus removal of snake case versions of class names) #minor



## [[`0.4.0+build.2`]] - 2022-05-04

### Fixed

- Triggering Linter on Tags Push Events



## [[`0.4.0+build.1`]] - 2022-05-04

### Changed

- Running Linters workflow on tags
- Running GitVersioniser on main branch, instead of `v0`



## [[`0.4.0`]] - 2022-05-04

### Changed

- Factory Name is now handled by Base Class #minor



## [[`0.3.3+build.7`]] - 2022-05-04

### Changed

- Commiting routines names were corrected to match their behaviour



## [[`0.3.3+build.6`]] - 2022-05-04

### Added

- Support for regular branch merge through GitHub (by reverse commit parent tree traversing)



## [[`0.3.3+build.5`]] - 2022-05-02

### Changed

- Routine "PushMainNew" to "PushMainNewCommit"
- Improved readability of options in `README.md`



## [[`0.3.3+build.4`]] - 2022-05-02

### Changed

- Checking for Commit Tags only in the first 5 letters at the beginning of a string
- Changed the increment values for alpha/beta/rc



## [[`0.3.3+build.3`]] - 2022-05-02

### Fixed

- Prerelease priority in comparison between semvers



## [[`0.3.3+build.2`]] - 2022-05-02

### Fixed

- Properly parsing changelog entries from commit description



## [[`0.3.3+build.1`]] - 2022-05-02

### Changed

- Changelog now also parses the commit description looking for the commit tags



## [[`0.3.3`]] - 2022-05-02

### Added

- Created wrapper for version #patch



## [[`0.3.2+build.10`]] - 2022-05-02

### Added

- Description property to Commit



## [[`0.3.2+build.9`]] - 2022-05-02

### Fixed

- Raising exception from the previous error



## [[`0.3.2+build.8`]] - 2022-05-02

### Changed

- Console Width set to 140 for stdout



## [[`0.3.2+build.7`]] - 2022-05-02

### Changed

- Updated Dependencies Versions



## [[`0.3.2+build.6`]] - 2022-05-02

### Changed

- Handling exception when versionised file can't be found



## [[`0.3.2+build.5`]] - 2022-05-02

### Added

- Code of Conduct



## [[`0.3.2+build.4`]] - 2022-05-02

### Changed

- Converted some methods to private staticmethods



## [[`0.3.2+build.3`]] - 2022-05-01

### Added

- More Increment Tags



## [[`0.3.2+build.2`]] - 2022-05-01

### Added

- Rich Logger



## [[`0.3.2+build.1`]] - 2022-05-01

### Changed

- Improved Printouts of VersioningResult in CI



## [[`0.3.2`]] - 2022-05-01

### Added

- New Routine: Prefix Tag with V #patch



## [[`0.3.1`]] - 2022-05-01

### Added

- New Routine: Should Contribute #patch



## [[`0.3.0+build.3`]] - 2022-05-01

### Added

- New Increment Type



## [[`0.3.0+build.2`]] - 2022-05-01

### Added

- New Commit Message Routines - Full Only Numbers



## [[`0.3.0+build.1`]] - 2022-04-30

### Changed

- Further Refactorization



## [[`0.3.0`]] - 2022-04-30

### Changed

- General Refactorization #minor



## [[`0.2.2+build.3`]] - 2022-04-30

### Added

- VersioningResult output printout



## [[`0.2.2+build.2`]] - 2022-04-30

### Changed

- Extracted exports of factory & abstract to `__init__.py`



## [[`0.2.2+build.1`]] - 2022-04-30

### Changed

- Extracted exports of `/core/` routines to `__init__.py`



## [[`0.2.2`]] - 2022-04-30

### Added

- Changelog Routine Tests #patch



## [[0.2.1+build.1]] - 2022-04-29

### Added

- Tests for Commiting



## [[0.2.1]] - 2022-04-29

### Added

- Tests for Commits Till Last Gitversioniser Commit #patch



## [[0.2.0+build.1]] - 2022-04-29

### Changed

- Arguments in `entrypoint.sh` are now named



## [[0.2.0]] - 2022-04-29

### Added

- Commit Messages Suffix/Prefix Variations #minor



## [[0.1.0+build.3]] - 2022-04-28

### Changed

- Start GitVersioniser after Markdown Linter succeeds



## [[0.1.0+build.2]] - 2022-04-28

### Added

- Markdown Linter & Link Checker



## [[0.1.0+build.1]] - 2022-04-28

### Changed

- Moved `test_*` files to `/core/` subdirectories



## [[0.1.0]] - 2022-04-28

### Added

- New Routine: `tagging` #minor



## [[0.0.2+build.6]] - 2022-04-28

### Changed

- Routines moved to subdirectory `/core/`



## [[0.0.2+build.5]] - 2022-04-28

### Fixed

- Changed path in `VersioniseFiles` to use config instead of hardcoded value



## [[0.0.2+build.4]] - 2022-04-27

### Fixed

- Links updated from `./src/*` to `./src/gitversioniser/*`



## [[0.0.2+build.3]] - 2022-04-27

### Changed

- Moved `main.py` outside `/src/` to parent dir



## [[0.0.2+build.2]] - 2022-04-27

### Added

- Tests for Commit Messages & File Updater



## [[0.0.2+build.1]] - 2022-04-27

### Changed

- Naming of GitVersioniser in .github/workflows



## [[0.0.2]] - 2022-04-27

### Changed

- Changelog `last_commit_as_summary`: Double Squared Brackets to Single Squared Brackets
- Moved `src` directories to `src/gitversioniser`
- Renamed `test` directory to `tests`
- Adjusted Repository for mypy #patch

### Added

- Environmental Configuration & Specifications
- Tests for Default Arguments
- Tests for Default Config



## [[0.0.1]] - 2022-04-27

### Fixed

- Adjusted the `\n` in changelog `CommitChangeTags` #patch



## [[0.0.0+build.2]] - 2022-04-27

### Changed

- GitVersioniser now runs after Python Linters succeed



## [[0.0.0+build.1]] - 2022-04-27

### Added

- Logo (500x500 & GH-Wide)



## [[0.0.0]] - 2022-04-26

**Repository Initialized**

[0.0.0]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.0.0
[0.0.0+build.1]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.0.0+build.1
[0.0.0+build.2]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.0.0+build.2
[0.0.1]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.0.1
[0.0.2]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.0.2
[0.0.2+build.1]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.0.2+build.1
[0.0.2+build.2]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.0.2+build.2
[0.0.2+build.3]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.0.2+build.3
[0.0.2+build.4]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.0.2+build.4
[0.0.2+build.5]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.0.2+build.5
[0.0.2+build.6]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.0.2+build.6
[0.1.0]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.1.0
[0.1.0+build.1]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.1.0+build.1
[0.1.0+build.2]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.1.0+build.2
[0.1.0+build.3]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.1.0+build.3
[0.2.0]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.2.0
[0.2.0+build.1]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.2.0+build.1
[0.2.1]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.2.1
[0.2.1+build.1]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.2.1+build.1
[`0.2.2`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.2.2
[`0.2.2+build.1`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.2.2+build.1
[`0.2.2+build.2`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.2.2+build.2
[`0.2.2+build.3`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.2.2+build.3
[`0.3.0`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.0
[`0.3.0+build.1`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.0+build.1
[`0.3.0+build.2`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.0+build.2
[`0.3.0+build.3`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.0+build.3
[`0.3.1`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.1
[`0.3.2`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.2
[`0.3.2+build.1`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.2+build.1
[`0.3.2+build.2`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.2+build.2
[`0.3.2+build.3`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.2+build.3
[`0.3.2+build.4`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.2+build.4
[`0.3.2+build.5`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.2+build.5
[`0.3.2+build.6`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.2+build.6
[`0.3.2+build.7`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.2+build.7
[`0.3.2+build.8`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.2+build.8
[`0.3.2+build.9`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.2+build.9
[`0.3.2+build.10`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.2+build.10
[`0.3.3`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.3
[`0.3.3+build.1`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.3+build.1
[`0.3.3+build.2`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.3+build.2
[`0.3.3+build.3`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.3+build.3
[`0.3.3+build.4`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.3+build.4
[`0.3.3+build.5`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.3+build.5
[`0.3.3+build.6`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.3+build.6
[`0.3.3+build.7`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.3.3+build.7
[`0.4.0`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.4.0
[`0.4.0+build.1`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.4.0+build.1
[`0.4.0+build.2`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.4.0+build.2
[`0.5.0`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.5.0
[`0.5.0+build.1`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.5.0+build.1
[`0.5.0+build.2`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.5.0+build.2
[`0.5.1`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.5.1
[`0.5.2`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.5.2
[`0.5.3`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.5.3
[`0.5.3+build.1`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.5.3+build.1
[`0.5.3+build.2`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.5.3+build.2
[`0.5.3+build.3`]: https://github.com/Luzkan/GitVersioniser/releases/tag/0.5.3+build.3
