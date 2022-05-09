#!/bin/sh -l

# -----------------
# Arguments:
# ----
# Versioniser Credentials
git_credential_username=$1      # [Git Credential]
git_credential_email=$2         # [Git Credential]
# ----
# Commit Tags
commit_increment_tags=$3        # [Tags]
commit_changelog_tags=$4        # [Tags]
# ----
# Versioning
routine_version=$5              # [Routine]
# ----
# Contributing
routine_should_contribute=$6    # [Routine]
routine_commiting=$7            # [Routine]
# ----
# Commit Message
routine_commit_message=$8       # [Routine]
# ----
# Tagging
routine_tagging=$9              # [Routine]
routine_prefix_tag_with_v=${10} # [Routine]
# ----
# Changelog
routine_changelog=${11}         # [Routine]
# ----
# File Updating
routine_file_updater=${12}      # [Routine]
versionised_files=${13}         # [Setting] For: routine_file_updater

# -----------------
# Git Configuration
git config --global --add safe.directory /github/workspace/target_repository
git config --global user.name "$git_credential_username"
git config --global user.email "$git_credential_email"

# -----------------
# Running the Script
cd target_repository
python -m pip install -e .
python /src/main.py -d . \
    --commit_increment_tags $commit_increment_tags \
    --commit_changelog_tags $commit_changelog_tags \
    --routine_version $routine_version \
    --routine_should_contribute $routine_should_contribute \
    --routine_commiting $routine_commiting \
    --routine_commit_message $routine_commit_message \
    --routine_tagging $routine_tagging \
    --routine_prefix_tag_with_v $routine_prefix_tag_with_v \
    --routine_changelog $routine_changelog \
    --routine_file_updater $routine_file_updater \
    --versioned_files $versionised_files
