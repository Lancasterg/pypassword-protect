from pathlib import Path, PosixPath
from enum import StrEnum

class FileExtensions:
    FILE_EXTENSION: str = ".prot"  # protected
    FILE_EXTENSION_LOCKED: str = ".locked"  # file is locked and encrypted
    FILE_EXTENSION_UNLOCKED: str = ".unlocked"



def _has_file_extension(file_path: str | Path | PosixPath, extension: FileExtensions) -> bool:
    if isinstance(file_path, str):
        file_path = Path(file_path)
    elif isinstance(file_path, PosixPath):
        file_path = Path(file_path)

    return file_path.suffix == extension


def has_prot_file_extension(file_path: str | Path | PosixPath) -> bool:
    pass
