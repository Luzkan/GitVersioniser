#!/bin/sh -l

# -----------------
# Arguments:

# $1 - [Git Credential] Username
# $2 - [Git Credential] Email Address
# ----
# Main
# ----
# $3 - [Routine] Version
# $4 - [Routine] Commiting
# $5 - [Routine] Tagging
# $6 - [Routine] Commit Messages
# ----
# Changelog
# ----
# $7 - [Routine] Changelog
# ----
# File Updating
# ----
# $8 - [Routine] File Updater
# $9 - [Setting] File List

# -----------------
# Git Configuration
git config --global --add safe.directory /github/workspace/target_repository
git config --global user.name "$1"
git config --global user.email "$2"

# -----------------
# Running the Script
cd target_repository
python /main.py -d . --routine_version $3 --routine_contribution $4 --routine_tagging $5 --routine_commit_message $5 --routine_file_updater $6 --routine_file_updater $7 --versioned_files $8
