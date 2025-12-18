import pytest

from importlib.resources import files
from pathlib import Path


@pytest.fixture
def tmp_files():
    return files("test.tmp_test_files")


@pytest.fixture
def teardown_delete_tmp_files():
    directory = Path(files("test.tmp_test_files").name)
    for file_path in directory.glob("*.prot"):
        if file_path.is_file():
            print()
            file_path.unlink()
            print(f"Deleted {file_path}")



# @pytest.fixture
# def teardown_delete_tmp_files():
#     """
#     Iterate over all .prot files in
#     """
#     test_files = files("test.tmp_test_files")
#     for item in test_files.iterdir():
#         if item.is_file() and "__init__.py" not in item.name:
#             test_file = Path(item.name)
#             if test_file.suffix == ".prot":
#                 print()
#                 test_file.unlink(missing_ok=True)

