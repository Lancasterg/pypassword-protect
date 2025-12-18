import base64
import os
from enum import StrEnum
from getpass import getpass

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Mode(StrEnum):
    ENCRYPT = "ENCRYPT"
    DECRYPT = "DECRYPT"


BACKEND = default_backend()
ITERATIONS = 100_000
SALT_SIZE = 16


def create_file(file_path: str) -> str:
    """
    Create a new file with the ".enc" file extension.

    Args:
        file_path: Path to the file to create

    Returns:
        (str): Full path to the created file
    """
    # if file_path[:3] != ".enc":
    #     file_path = f"{file_path}.enc"
    open(file_path, "w")
    return file_path



#
# def derive_key(password: str, salt: bytes) -> bytes:
#     kdf = PBKDF2HMAC(
#         algorithm=hashes.SHA256(),
#         length=32,
#         salt=salt,
#         iterations=ITERATIONS,
#         backend=BACKEND,
#     )
#     return base64.urlsafe_b64encode(kdf.derive(password.encode()))
#
#
# def encrypt_file(filename: str) -> None:
#     password = getpass("Enter password: ")
#     confirm = getpass("Confirm password: ")
#
#     if password != confirm:
#         raise ValueError("Passwords do not match")
#
#     salt = os.urandom(SALT_SIZE)
#     key = derive_key(password, salt)
#     fernet = Fernet(key)
#
#     with open(filename, "rb") as f:
#         data = f.read()
#
#     encrypted = fernet.encrypt(data)
#
#     with open(filename + ".enc", "wb") as f:
#         f.write(salt + encrypted)
#
#     print(f"Encrypted → {filename}.enc")
#
#
# def decrypt_file(filename: str):
#     password = getpass("Enter password: ")
#
#     with open(filename, "rb") as f:
#         salt = f.read(SALT_SIZE)
#         encrypted_data = f.read()
#
#     key = derive_key(password, salt)
#     fernet = Fernet(key)
#
#     try:
#         decrypted = fernet.decrypt(encrypted_data)
#     except Exception:
#         raise ValueError("Incorrect password or corrupted file")
#
#     output_file = filename.replace(".enc", ".dec")
#     with open(output_file, "wb") as f:
#         f.write(decrypted)
#
#     print(f"Decrypted → {output_file}")
#
