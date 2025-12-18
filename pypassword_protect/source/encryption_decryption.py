import base64
import os
from enum import StrEnum
from getpass import getpass


class CurrentState(StrEnum):
    UNLOCKED = "unlocked"
    LOCKED = "locked"


def create_file(file_path: str) -> str:
    """
    Create a new file with the ".enc" file extension.

    Args:
        file_path: Path to the file to create

    Returns:
        (str): Full path to the created file
    """
    open(file_path, "w")
    return file_path

