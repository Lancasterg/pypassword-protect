import base64
import os
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


SALT_SIZE: int = 16


class BadPasswordException(Exception): ...


def _derive_key(password: str, salt: bytes) -> bytes:
    """
    Derive a key from a password (string)
    Args:
        password: A string to derive the key from
        salt: random 16-byte value

    Returns:
        (bytes) A fresh, random 16-byte value that can be prepended to a file

    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend(),
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def is_locked(file_path: str) -> bool:
    """
    Check whether a file appears to be locked (encrypted) by this tool.

    This does NOT verify the password.

    Args:
        file_path: The path to the file to check

    Returns:
        bool: True if the file is locked, False otherwise
    """
    try:
        with open(file_path, "rb") as f:
            blob = f.read()

        if len(blob) <= SALT_SIZE:
            return False

        encrypted_data = blob[SALT_SIZE:]

        # Fernet tokens are URL-safe base64
        # and always start with b"gAAAAAB"
        if not encrypted_data.startswith(b"gAAAAAB"):
            return False

        # Validate base64 structure
        base64.urlsafe_b64decode(encrypted_data)

        return True

    except Exception as e:
        return False


def file_exists(file_path: str) -> bool:
    """
    Checks to see if a file exists
    Args:
        file_path: The path to the file

    Returns:
        bool: True if the file exists, False otherwise

    """
    return Path(file_path).is_file()


def lock_file(file_path: str, password: str, output_location: str) -> None:
    """
    Lock (encrypt) a file using a password.

    Args:
        file_path: Path to the file to unlock
        password: The password to decrypt the file with
        output_location: The location to output the locked file

    Returns:
        None

    """
    with open(file_path, "rb") as f:
        data = f.read()

    salt = os.urandom(SALT_SIZE)
    key = _derive_key(password, salt)
    fernet = Fernet(key)

    encrypted_data = fernet.encrypt(data)

    # Store salt + ciphertext
    with open(output_location, "wb") as open_file:
        open_file.write(salt + encrypted_data)


def unlock_file(
    file_path: str, password: str, output_location: str
) -> None:
    """
    Unlock (decrypt) a file using a password.

    Args:
        file_path: Path to the file to unlock
        password: The password to decrypt the file with
        output_location: The location to output the unlocked file

    Returns:
        None

    """
    with open(file_path, "rb") as open_file:
        blob = open_file.read()

    if len(blob) < SALT_SIZE:
        raise ValueError("Invalid or corrupted file")

    salt = blob[:SALT_SIZE]
    encrypted_data = blob[SALT_SIZE:]

    key = _derive_key(password, salt)
    fernet = Fernet(key)

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except InvalidToken as e:
        raise BadPasswordException("Password does not match") from e

    with open(output_location, "wb") as open_file:
        open_file.write(decrypted_data)
