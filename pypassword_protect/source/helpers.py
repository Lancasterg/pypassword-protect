from pathlib import Path, PosixPath

FILE_EXTENSION: str = ".prot"


def has_prot_file_extension(file_path: str | Path | PosixPath) -> bool:
    if isinstance(file_path, str):
        file_path = Path(file_path)
    elif isinstance(file_path, PosixPath):
        file_path = Path(file_path)

    return file_path.suffix == FILE_EXTENSION
