
import os
import string
from cryptography.fernet import Fernet
import ctypes

def load_key():
    return open("secret.key", "rb").read()

def decrypt_file(file_path, key):
    try:
        fernet = Fernet(key)
        with open(file_path, "rb") as file:
            encrypted = file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted)
    except Exception as e:
        print(f"[!] Failed to decrypt {file_path}: {e}")

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            if file == "secret.key":
                continue
            elif file == "README.txt":
                os.remove(full_path)
                print(f"[-] Deleted ransom note: {full_path}")
            else:
                decrypt_file(full_path, key)

def main():
    if not os.path.exists("secret.key"):
        print("[-] secret.key not found! Cannot decrypt.")
        return

    key = load_key()
    found_any = False
    for drive_letter in string.ascii_uppercase:
        drive = f"{drive_letter}:/"
        if os.path.exists(drive):
            for root, dirs, _ in os.walk(drive):
                for dir in dirs:
                    if dir == "test_folder":
                        folder_path = os.path.join(root, dir)
                        print(f"[+] Found test_folder at: {folder_path}")
                        decrypt_folder(folder_path, key)
                        print(f"[✔] Decrypted: {folder_path}\n")
                        found_any = True
    if not found_any:
        print("[-] No test_folder found on any drive.")

    try:
        long_message = (
            "✅ YOUR FILES HAVE BEEN DECRYPTED ✅\n\n"
            "=========================================\n"
            "All encrypted files have been successfully restored.\n\n"
            "Please backup your data regularly.\n"
            "This was a simulation for educational purposes.\n\n"
            "Stay safe! 🛡️"
        )
        ctypes.windll.user32.MessageBoxW(
            0,
            long_message,
            "Decryption Complete",
            0x40 | 0x0  # Info icon, OK button
        )
    except:
        pass

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()