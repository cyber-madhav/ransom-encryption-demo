```bash
# 🛡️ Ransomware Simulation – Educational Project

> **⚠️ WARNING – EDUCATIONAL USE ONLY**  
> This tool is designed to **simulate ransomware behavior in a safe, controlled way**.  
> It **only** encrypts files inside folders named exactly `test_folder`.  
> Do **not** modify the safety filters – doing so may cause permanent data loss.  
> The author is not responsible for any misuse or damage.

---

## 📖 Overview

This project contains two Python scripts that mimic how file‑encrypting ransomware works:

- **`encrypt.py`** – Scans all drives for folders named `test_folder`, encrypts every file inside them (using Fernet symmetric encryption), and drops a ransom note (`README.txt`).
- **`decrypt.py`** – Uses the same encryption key to restore all encrypted files and delete the ransom notes.

The purpose is purely **educational**: to understand ransomware mechanics, file encryption, drive traversal, and the importance of backups – all in a completely reversible, harmless environment.

---

## 🔧 Requirements

- Python 3.6 or higher
- `cryptography` library

Install the dependency:


pip install cryptography
```
🚀 Quick Start
1️⃣ Create a test folder
Create a folder named test_folder anywhere on your system (e.g., C:\test_folder or D:\my_files\test_folder).
Place some dummy files inside (text files, images, etc.) – nothing important.

2️⃣ Run the encryption (simulated attack)
bash
python encrypt.py
The script generates a secret.key file in the current directory.

It finds all test_folder directories on any drive (A:\ to Z:).

Every file in those folders is encrypted (overwritten).

A ransom note README.txt appears inside each test_folder.

3️⃣ Verify the effect
Open the test_folder – files are now unreadable (garbled). The ransom note explains the “attack”.

4️⃣ Decrypt your files
bash
python decrypt.py
The script uses secret.key to decrypt every file inside all test_folder directories.

All ransom notes are deleted automatically.

Your original files are fully restored.

5️⃣ Clean up
Delete secret.key and the test_folder directories (or keep them for future tests).

🛡️ Critical Safety Features
The encryption script only affects folders with the exact name test_folder:

python
if dir == "test_folder":     # ← never change this condition
    encrypt_folder(folder_path, fernet)
No system files are ever touched.

No persistence, no network – the script does not install itself or communicate externally.

Full reversibility – decryption is always possible with the correct key.

❗ Modifying or removing the test_folder check will encrypt all files on all drives – including Windows system files – making your computer unbootable.
You have been warned.

🧪 Customization (Safe Changes)
You can safely modify the following without breaking the safety guard:

Change	How to do it
Target a different folder name	Replace "test_folder" with "my_safe_dir" (in both scripts)
Change the ransom note text	Edit the note_content string in encrypt.py
Add more files to skip	Extend the if file in ["secret.key", "README.txt"] condition
Remove Windows message boxes	Comment out the ctypes.windll.user32.MessageBoxW block
Run on Linux/macOS	Works fine – just remove the ctypes part or install python3-tk for alerts
🐛 Troubleshooting
Problem	Solution
ModuleNotFoundError: No module named 'cryptography'	Run pip install cryptography
secret.key not found when decrypting	Make sure decrypt.py is in the same folder as secret.key
No test_folder found	Double‑check the spelling and location – the name is case‑sensitive on Linux/macOS
Permission denied (Windows)	Run as a normal user; avoid system folders like C:\Windows (the script automatically skips errors)
Message box doesn’t appear	This is Windows‑only; ignore or replace with print()
📁 Repository Structure
text
.
├── encrypt.py          # Simulated ransomware
├── decrypt.py          # Decryption tool
├── secret.key          # Generated on first run – keep safe!
├── README.md           # This file
└── LICENSE             (optional, e.g., MIT with ethical use clause)
📜 Legal & Ethical Notice
This code is intended solely for educational purposes in a controlled environment (your own computer or an isolated virtual machine).

Using similar techniques to encrypt, ransom, or damage data belonging to others is a serious crime (ransomware attack) and violates GitHub’s Acceptable Use Policies.

The author assumes no liability for misuse. By using this code, you agree to use it responsibly and only for learning.

📄 License
MIT – but with the explicit ethical restriction that this software must not be used for malicious purposes.
See the full license text in LICENSE (if included).

🙏 Acknowledgments
cryptography library for the Fernet symmetric encryption.

Educational resources on ransomware defense and cybersecurity awareness.

Stay safe, back up your data, and never run untrusted code on important machines. 🛡️
