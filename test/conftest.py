import pytest

from importlib.resources import files
from pathlib import Path


@pytest.fixture
def tmp_files():
    return files("test.tmp_test_files")


@pytest.fixture()
def teardown_delete_tmp_files():
    """
    Fixture for deleting all files in test/tmp_test_files/*.prot
    """
    ...
    yield
    directory = Path(files("test.tmp_test_files").name)
    for file_path in directory.glob("*.prot"):
        if file_path.is_file():
            file_path.unlink()
