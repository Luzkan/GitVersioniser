#!/bin/sh -l

# -----------------
# Arguments:
# ----
# Versioniser Credentials
git_credential_username=$1      # [Git Credential]
git_credential_email=$2         # [Git Credential]
# ----
# Contributing
routine_commiting=$3            # [Routine]
routine_tagging=$4              # [Routine]
# ----
# Versionising
routine_version=$5              # [Routine]
# ----
# Commit Message
routine_commit_message=$6       # [Routine]
# ----
# Changelog
routine_changelog=$7            # [Routine]
# ----
# File Updating
routine_file_updater=$8         # [Routine]
versionised_files=$9            # [Setting] For: routine_file_updater

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
    --routine_commiting $routine_commiting \
    --routine_tagging $routine_tagging \
    --routine_version $routine_version \
    --routine_commit_message $routine_commit_message \
    --routine_changelog $routine_changelog \
    --routine_file_updater $routine_file_updater \
    --versioned_files $versionised_files
