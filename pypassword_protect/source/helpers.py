from pathlib import Path
import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SALT_SIZE: int = 16


def _derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend(),
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def create_file(path: str, password: str, locked: bool = True) -> str:
    # Create file if not exists
    if not Path(path).exists():
        open(path, "w")
    else:
        raise IOError("File already exists")

    if locked is True:
        lock_file(path, password)

    return path


def lock_file(file_path: str, password: str) -> None:
    with open(file_path, "rb") as f:
        data = f.read()

    salt = os.urandom(SALT_SIZE)
    key = _derive_key(password, salt)
    fernet = Fernet(key)

    encrypted_data = fernet.encrypt(data)

    # Store salt + ciphertext
    with open(file_path, "wb") as f:
        f.write(salt + encrypted_data)


def unlock_file(file_path: str, password: str, output_location: str | None = None) -> None:
    with open(file_path, "rb") as open_file:
        blob = open_file.read()

    if len(blob) < SALT_SIZE:
        raise ValueError("Invalid or corrupted file")

    salt = blob[:SALT_SIZE]
    encrypted_data = blob[SALT_SIZE:]

    key = _derive_key(password, salt)
    fernet = Fernet(key)

    decrypted_data = fernet.decrypt(encrypted_data)

    if output_location is None:
        write_location = file_path
    else:
        write_location = output_location

    with open(write_location, "wb") as open_file:
        open_file.write(decrypted_data)

