from cryptography.fernet import Fernet
from pathlib import Path

KEY_FILE = Path("secret.key")


def generate_key():
    key = Fernet.generate_key()
    KEY_FILE.write_bytes(key)
    print("New encryption key created: secret.key")


def load_key():
    if not KEY_FILE.exists():
        print("No encryption key found.")
        print("Generate a key first.")
        return None

    return KEY_FILE.read_bytes()


def encrypt_message(message, key):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode()).decode()


def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)

    try:
        return cipher.decrypt(encrypted_message.encode()).decode()
    except Exception:
        return None


def encrypt_file(file_path, key):
    path = Path(file_path)

    if not path.exists():
        print("File not found.")
        return

    data = path.read_bytes()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)

    output_path = Path(str(path) + ".encrypted")
    output_path.write_bytes(encrypted_data)

    print(f"File encrypted successfully:")
    print(output_path)


def decrypt_file(file_path, key):
    path = Path(file_path)

    if not path.exists():
        print("Encrypted file not found.")
        return

    try:
        encrypted_data = path.read_bytes()

        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data)

        if path.name.endswith(".encrypted"):
            output_name = path.name[:-10]
        else:
            output_name = path.name + ".decrypted"

        output_path = path.parent / output_name
        output_path.write_bytes(decrypted_data)

        print("File decrypted successfully:")
        print(output_path)

    except Exception:
        print("Unable to decrypt the file.")
        print("Make sure you are using the correct encryption key.")


def main():
    print("=" * 45)
    print("       ENCRYPTED ELKANEMI v2.0")
    print("=" * 45)

    while True:
        print("\n1. Generate encryption key")
        print("2. Encrypt message")
        print("3. Decrypt message")
        print("4. Encrypt file")
        print("5. Decrypt file")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            generate_key()

        elif choice == "2":
            key = load_key()

            if key:
                message = input("Enter message: ")
                encrypted = encrypt_message(message, key)

                print("\nEncrypted message:")
                print(encrypted)

        elif choice == "3":
            key = load_key()

            if key:
                encrypted_message = input("Enter encrypted message: ")
                decrypted = decrypt_message(encrypted_message, key)

                if decrypted is None:
                    print("Unable to decrypt the message.")
                else:
                    print("\nDecrypted message:")
                    print(decrypted)

        elif choice == "4":
            key = load_key()

            if key:
                file_path = input("Enter the file path: ")
                encrypt_file(file_path, key)

        elif choice == "5":
            key = load_key()

            if key:
                file_path = input("Enter the encrypted file path: ")
                decrypt_file(file_path, key)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()