# Auto-Folder-Structure-Generator--PowerShell-Python
A cross-platform Python utility that audits user-profile directories and automatically provisions a standardised 8-folder structure, without ever overwriting existing data.


📌 **Overview**


Managing consistent folder structures across multiple user profiles is a common sysadmin challenge. This project started life as a Windows PowerShell script and has been rewritten in pure Python to run on Windows, macOS, and Linux with zero external dependencies.
The script walks every user folder inside a configurable base directory, checks for 8 required sub-folders, creates any that are missing, and for two specific folders - also provisions four nested sub-folders each.


---
🗂️ Required Folder Structure Created
```
<BASE_DIR>/
└── <UserFolder>/
    ├── Alias/
    ├── Certificates/
    ├── Eco/
    ├── Examination/
    │   ├── Sub_Folder_01/
    │   ├── Sub_Folder_02/
    │   ├── Sub_Folder_03/
    │   └── Sub_Folder_04/
    ├── Health and Safety/
    │   ├── Sub_Folder_01/
    │   ├── Sub_Folder_02/
    │   ├── Sub_Folder_03/
    │   └── Sub_Folder_04/
    ├── Meetings/
    ├── Services/
    └── Training/
```

---


⚙️ **How It Works**
1. Logging - a timestamped `.log` file is created at startup (mirrors PowerShell's `Start-Transcript`).
2. Discovery - the script scans the base directory for immediate child directories (user profile folders).
3. Audit & Create - for every user folder, each of the 8 required folders is checked; missing ones are created with `os.makedirs(exist_ok=True)` so existing data is never touched.
4. Nested folders - `Examination` and `Health and Safety` each receive 4 sub-folders automatically.
5. Log closure - a final log entry marks the end of the run.


---
🚀 **Getting Started**

Prerequisites
Python 3.7+
No third-party packages required
Installation
```bash
git clone https://github.com/<your-username>/auto-folder-structure-generator.git
cd auto-folder-structure-generator
```
Configuration
Open `create_folders.py` and update the two constants near the top:
```python
BASE_DIR = r"C:\Temp\Upwork\YB"   # path containing user profile folders
LOG_DIR  = BASE_DIR                # where log files are saved
```
Run
```bash
python create_folders.py
```


🙋 Author
Mark Thomas Bundang 
https://github.com/tab8/
