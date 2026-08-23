# 🔐 Encrypted-Elkanemi

A Python-based encryption and decryption tool built for learning practical cryptography and cybersecurity concepts.

## 🚀 Features

* Generate secure encryption keys
* Encrypt text messages
* Decrypt encrypted messages
* Store encryption keys locally
* Simple command-line interface
* Uses the Python `cryptography` library

## 🛠️ Technologies

* Python
* Cryptography
* Fernet symmetric encryption
* Git & GitHub

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/tijjania/Encrypted-Elkanemi.git
```

Enter the project directory:

```bash
cd Encrypted-Elkanemi
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the program:

```bash
python encryptor.py
```

You will see:

```text
========================================
      ENCRYPTED ELKANEMI v1.0
========================================

1. Generate encryption key
2. Encrypt message
3. Decrypt message
4. Exit
```

### Generate a key

Select option `1`.

The program will create:

```text
secret.key
```

**Keep this file private.**

### Encrypt a message

Select option `2` and enter your message.

The program will generate encrypted text that can only be decrypted using the correct key.

### Decrypt a message

Select option `3` and enter the encrypted message.

The original message will be recovered if the correct key is available.

## 🔒 Security

This project is intended for educational purposes.

The encryption key is stored locally and is excluded from Git using `.gitignore`.

**Never upload your `secret.key` to GitHub or share it publicly.**

## 📚 Learning Objectives

This project helps demonstrate practical understanding of:

* Symmetric encryption
* Encryption keys
* Secure key handling
* Python programming
* Cryptography libraries
* Git and GitHub
* Basic cybersecurity principles

## 🎯 Future Improvements

* [ ] Encrypt files
* [ ] Decrypt files
* [ ] Add password-based key derivation
* [ ] Improve error handling
* [ ] Add automated tests
* [ ] Create a graphical user interface
* [ ] Add logging and security checks

## 👨‍💻 Author

**Tijjani**

GitHub: [@tijjania](https://github.com/tijjania)

---

### ⚠️ Disclaimer

This project is created for educational and defensive cybersecurity learning purposes. It should not be used to conceal or facilitate illegal activity.
