"""
create_folders.py

Checks each user profile folder under a specified base directory for 8 required
sub-folders. Creates any that are missing without overwriting existing data.
Sub-folders within 'Examination' and 'Health and Safety' are also created if absent.

Author  : (Your Name)
Version : 1.0.0
"""

import os
import logging
from datetime import datetime

# ── Configuration ─────────────────────────────────────────────────────────────

BASE_DIR = r"C:\Temp\Upwork\YB"          # Root directory containing user folders
LOG_DIR  = BASE_DIR                       # Transcript / log output location

REQUIRED_FOLDERS = [
    "Alias",
    "Certificates",
    "Eco",
    "Examination",
    "Health and Safety",
    "Meetings",
    "Services",
    "Training",
]

# Nested sub-folders required inside specific parent folders
NESTED_SUBFOLDERS = {
    "Examination":      ["Sub_Folder_01", "Sub_Folder_02", "Sub_Folder_03", "Sub_Folder_04"],
    "Health and Safety":["Sub_Folder_01", "Sub_Folder_02", "Sub_Folder_03", "Sub_Folder_04"],
}

# ── Logging setup ─────────────────────────────────────────────────────────────

def setup_logging(log_dir: str) -> None:
    """Configure logging to both console and a timestamped log file."""
    os.makedirs(log_dir, exist_ok=True)
    timestamp   = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file    = os.path.join(log_dir, f"Create_Folders_{timestamp}.log")

    logging.basicConfig(
        level   = logging.INFO,
        format  = "%(asctime)s  %(levelname)-8s  %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
        handlers = [
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),          # mirrors Start-Transcript to console
        ],
    )
    logging.info("Transcript started  →  %s", log_file)


# ── Core logic ────────────────────────────────────────────────────────────────

def create_folder(path: str) -> None:
    """Create *path* if it does not already exist (never overwrites)."""
    if os.path.exists(path):
        logging.info("    EXISTS  – skipping  : %s", path)
    else:
        os.makedirs(path, exist_ok=True)      # exist_ok avoids race conditions
        logging.info("    CREATED             : %s", path)


def process_user_folder(user_folder: str) -> None:
    """Ensure all required folders (and nested sub-folders) exist for one user."""
    logging.info("Working on USER Folder : %s", user_folder)

    for folder_name in REQUIRED_FOLDERS:
        logging.info("  Working on Sub-Folder: %s", folder_name)
        folder_path = os.path.join(user_folder, folder_name)

        # Create the top-level required folder
        create_folder(folder_path)

        # Create any mandatory nested sub-folders
        if folder_name in NESTED_SUBFOLDERS:
            for sub in NESTED_SUBFOLDERS[folder_name]:
                create_folder(os.path.join(folder_path, sub))


def main() -> None:
    setup_logging(LOG_DIR)
    logging.info("Base directory : %s", BASE_DIR)

    if not os.path.isdir(BASE_DIR):
        logging.error("Base directory does not exist: %s", BASE_DIR)
        return

    # Iterate over every direct child directory (= user profile folders)
    user_folders = [
        entry.path
        for entry in os.scandir(BASE_DIR)
        if entry.is_dir()
    ]

    if not user_folders:
        logging.warning("No user folders found in %s", BASE_DIR)
        return

    for user_folder in sorted(user_folders):
        process_user_folder(user_folder)

    logging.info("Transcript stopped.")


if __name__ == "__main__":
    main()
