from importlib.resources import files
from pathlib import Path

import pytest


@pytest.fixture
def tmp_files():
    return files("test.tmp_test_files")


@pytest.fixture
def teardown_delete_tmp_files():
    """
    Fixture for deleting all files in test/tmp_test_files/*.prot
    """
    ...
    yield
    directory = Path(files("test.tmp_test_files").name)
    for file_path in directory.glob("*.test"):
        if file_path.is_file():
            file_path.unlink()


@pytest.fixture
def create_tmp_file_unlocked():
    file_path = str(files("test.tmp_test_files").joinpath("tmp_file_unlocked.test"))

    # Convert to filesystem path and create the file
    with open(file_path, "w") as f:
        f.write("")

    yield file_path
    ...
