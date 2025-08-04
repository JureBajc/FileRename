# Rename and Organize Media Files

This Python script automates the renaming and organization of files and folders in a directory by applying a consistent naming convention based on detected or metadata dates.

---

## 📄 Features

- 🔎 **Auto-detects dates** from file names or metadata (supports `YYYY-MM-DD` and `DD.MM.YYYY`)
- 📂 **Processes folders recursively** (or just one, optionally)
- 📝 **Renames to format:** `DD-MM-YYYY_ZZZ_LANG_KratekOpis.ext`
- ⚠️ **Handles name conflicts** by appending suffixes (_1, _2, etc.)
- 🔍 **Dry-run mode** to preview changes before applying
- 📜 Logs all operations to `seznam_rename.txt`

---

## 🛠️ Usage

### 1. Set the main directory

In the script:
```python
start_dir = r'H:\VIDEO PREDSTAVITVE'  # <- Set your root directory here
```

### 2. Adjust options

```python
dry_run = True  # Simulate without renaming files
test_single_folder_only = True  # Process only the specified folder, skip subfolders
```

### 3. Run the script

```bash
python rename_script.py
```

---

## 🧠 Naming Format

Renamed files will follow this convention:

```
DD-MM-YYYY_ZZZ_LANG_KratekOpis.ext
```

- **DD-MM-YYYY**: Date from filename or metadata
- **ZZZ**: Placeholder for internal code (e.g., department or type)
- **LANG**: Language or localization code
- **KratekOpis**: Cleaned version of the original name (underscored)

---

## 🧪 Example

**Before:**
```
video_2023-08-04.mp4
```

**After (real run):**
```
04-08-2023_ZZZ_LANG_video.mp4
```

**Log output:**
```
H:\VIDEO PREDSTAVITVE\video_2023-08-04.mp4 -> H:\VIDEO PREDSTAVITVE\04-08-2023_ZZZ_LANG_video.mp4
```

---

## 📁 Output

- Renamed files and folders in the original directory
- `seznam_rename.txt`: Log of all operations (including errors and simulations)

---

## 📋 Requirements

- Python 3.6+
- Works best on Windows paths (uses `os.path`)

---

## ⚠️ Limitations

- Requires that filenames contain a valid date or that file metadata is accessible
- Only basic error handling (e.g., for locked or unreadable files)

---

## 🚀 Installation & Setup

1. **Download the script** to your desired location
2. **Install Python 3.6+** if not already installed
3. **Configure the script**:
   - Set your `start_dir` path
   - Adjust `dry_run` and `test_single_folder_only` options
4. **Run a test** with `dry_run = True` first to preview changes
5. **Execute for real** by setting `dry_run = False`

---

## 🔧 Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `start_dir` | string | `r'H:\VIDEO PŘEDSTAVITVE'` | Root directory to process |
| `dry_run` | boolean | `True` | Preview mode - no actual renaming |
| `test_single_folder_only` | boolean | `True` | Process only root folder (no recursion) |

---

## 📊 Supported Date Formats

The script automatically detects and converts these date formats:

- `YYYY-MM-DD` (e.g., 2023-08-04)
- `DD.MM.YYYY` (e.g., 04.08.2023)
- File metadata dates (creation/modification timestamps)

---

## 🛡️ Safety Features

- **Dry-run mode**: Test all operations before executing
- **Conflict resolution**: Automatic suffix addition for duplicate names
- **Comprehensive logging**: All operations recorded in `seznam_rename.txt`
- **Error handling**: Graceful handling of locked or inaccessible files

---

## 📝 Log File Format

The `seznam_rename.txt` log includes:

- **Successful renames**: `Original_path -> New_path`
- **Dry-run simulations**: `[DRY RUN] Original_path -> New_path`
- **Errors**: `ERROR: Description of issue`
- **Timestamps**: When operations occurred

---

## 🔍 Troubleshooting

### Common Issues

**Q: Script doesn't find any dates**
- A: Ensure filenames contain `YYYY-MM-DD` or `DD.MM.YYYY` format
- A: Check that files have accessible metadata timestamps

**Q: "Permission denied" errors**
- A: Close any programs using the files
- A: Run as administrator if necessary
- A: Check file/folder permissions

**Q: Names get truncated**
- A: Windows path length limit (260 chars) - move to shorter directory

### Best Practices

1. **Always test first** with `dry_run = True`
2. **Backup important files** before running
3. **Close media players** and other programs using the files
4. **Check the log file** after each run for any errors

---

## 📜 License

MIT License – free to use, modify, and distribute.

---

## 🤝 Contributing

Feel free to:
- Report bugs or issues
- Suggest new features
- Submit improvements
- Share your use cases

---

## 📞 Support

For questions or issues:
1. Check the troubleshooting section above
2. Review the log file (`seznam_rename.txt`) for error details
3. Test with a small subset of files first
4. Ensure all file paths are accessible and not in use

---

*Last updated: August 2025*
