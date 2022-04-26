#!/bin/sh -l

# -----------------
# Arguments:

# $1 - [Git Credential] Username
# $2 - [Git Credential] Email Address
# ----
# Main
# ----
# $3 - [Routine] Version
# $4 - [Routine] Contribution
# $5 - [Routine] Commit Messages
# ----
# Changelog
# ----
# $6 - [Routine] Changelog
# ----
# File Updating
# ----
# $7 - [Routine] File Updater
# $8 - [Setting] File List

# -----------------
# Git Configuration
git config --global --add safe.directory /github/workspace/target_repository
git config --global user.name "$1"
git config --global user.email "$2"

# -----------------
# Running the Script
cd target_repository
python /src/main.py -d . --routine_version $3 --routine_contribution $4 --routine_commit_message $5 --routine_file_updater $6 --routine_file_updater $7 --versioned_files $8
