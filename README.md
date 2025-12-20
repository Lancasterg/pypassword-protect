# pypassword-encryption

`pypassword-encryption` is a simple command-line tool for encrypting and decrypting files using a password.

## Installation

To install the `passprotect` binary:

1.  **Download the binary:**
    The `passprotect` executable is provided in the `bin/` directory. You can download it directly from the project's releases or clone the repository.

2.  **Move the binary to your PATH:**
    ```bash
    sudo mv bin/passprotect /usr/local/bin/
    ```
    This moves the `passprotect` executable to `/usr/local/bin/`, making it accessible from any directory in your terminal.

    Alternatively, you can add the `bin/` directory to your `PATH` environment variable:
    ```bash
    export PATH=$PATH:/path/to/passprotect/bin
    ```
    (Replace `/path/to/pypassword-encryption` with the actual path to your cloned repository.)

## Usage

Once installed, you can use `passprotect` to lock and unlock your files.

### Locking a file

To encrypt a file, use the `lock` command:

```bash
passprotect -l <filename>
```

You will be prompted to enter a password, which will be used to encrypt the file.

### Unlocking a file

To decrypt a file, use the `unlock` command:

```bash
passprotect -u <filename>
```

You will be prompted to enter the password used during encryption. If the password is correct, the file will be decrypted.

## How it works

`pypassword-encryption` uses the `cryptography.fernet` library, which implements symmetric encryption. Here's a brief overview:

1.  **Key Derivation:** When you provide a password, a unique encryption key is derived from it using `PBKDF2HMAC` (Password-Based Key Derivation Function 2 with HMAC). This process involves combining your password with a randomly generated 16-byte "salt" and performing many iterations of a hashing algorithm (SHA256). The salt is crucial for security, as it ensures that even if two users have the same password, their derived encryption keys will be different.

2.  **Encryption:** The derived key is then used by Fernet to encrypt the file's contents. Fernet is a high-level cryptographic primitive that handles many details of secure encryption, including using strong algorithms and ensuring message authenticity.

3.  **File Storage:** The encrypted data is stored in the file, prefixed with the 16-byte salt that was used during key derivation. This allows the `passprotect` tool to retrieve the correct salt when you try to unlock the file, ensuring the same key can be derived for decryption.

4.  **Decryption:** When unlocking, the tool reads the salt from the beginning of the file, derives the key using your provided password and the stored salt, and then uses this key to decrypt the file's contents. If the password is incorrect, the decryption will fail, and a `BadPasswordException` will be raised.
