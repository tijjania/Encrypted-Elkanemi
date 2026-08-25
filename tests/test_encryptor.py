from cryptography.fernet import Fernet

from encryptor import (
    encrypt_message,
    decrypt_message,
    encrypt_file,
    decrypt_file,
)


def test_message_encryption():
    key = Fernet.generate_key()
    message = "Hello Tijjani"

    encrypted = encrypt_message(message, key)

    assert encrypted != message

    decrypted = decrypt_message(encrypted, key)

    assert decrypted == message


def test_invalid_message():
    key = Fernet.generate_key()

    result = decrypt_message("invalid encrypted text", key)

    assert result is None


def test_file_encryption_and_decryption(tmp_path):
    key = Fernet.generate_key()

    original = tmp_path / "hello.txt"
    original.write_text("Encrypted Elkanemi Test")

    encrypt_file(original, key)

    encrypted_file = tmp_path / "hello.txt.encrypted"

    assert encrypted_file.exists()
    assert encrypted_file.read_bytes() != original.read_bytes()

    decrypt_file(encrypted_file, key)

    restored = tmp_path / "hello.txt"

    assert restored.exists()
    assert restored.read_text() == "Encrypted Elkanemi Test"