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


def main():
    print("=" * 40)
    print("      ENCRYPTED ELKANEMI v1.0")
    print("=" * 40)

    while True:
        print("\n1. Generate encryption key")
        print("2. Encrypt message")
        print("3. Decrypt message")
        print("4. Exit")

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
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
