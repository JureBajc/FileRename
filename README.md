name: Rename and Organize Media Files
description: >
  This script scans a directory of video/document files and renames them
  using a standard format: DD-MM-YYYY_ZZZ_LANG_KratekOpis.ext.
  Dates can be extracted from the file name or metadata. The process can run in dry-run mode for simulation.

author: your-name
version: 1.0.0
license: MIT
entry_point: rename_script.py
language: Python
requirements:
  - python>=3.6
usage:
  command: python rename_script.py
  arguments:
    - start_dir: Path to the directory you want to scan and rename (default: H:\VIDEO PREDSTAVITVE)
    - dry_run: Set to True to simulate changes without renaming files
    - test_single_folder_only: Process only the specified folder, not subfolders
outputs:
  - seznam_rename.txt: Log file with results of renaming or simulation
features:
  - Recursively renames files and folders based on detected or metadata date
  - Standardizes file names to: DD-MM-YYYY_ZZZ_LANG_KratekOpis
  - Handles naming conflicts automatically (e.g., appends _1, _2, etc.)
  - Logs all renaming actions or issues
  - Simulation mode to preview changes before applying
patterns_detected:
  - Date formats in file names: YYYY-MM-DD, DD.MM.YYYY
  - Cleans redundant spacing and date stamps from names
limitations:
  - Assumes filenames contain a recognizable date or valid file metadata
  - Only supports Windows-style file paths by default
