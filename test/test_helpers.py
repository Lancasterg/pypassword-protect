from passprotect.helpers import has_prot_file_extension
from pathlib import Path, PosixPath


def test_has_prot_file_extension_str_true():
    file_path = "a/path/to/a/file/file.prot"

    assert has_prot_file_extension(file_path) is True


def test_has_prot_file_extension_path_true():
    file_path = Path("a/path/to/a/file/file.prot")

    assert has_prot_file_extension(file_path) is True


def test_has_prot_file_extension_posix_path_true():
    file_path = PosixPath("a/path/to/a/file/file.prot")

    assert has_prot_file_extension(file_path) is True


def test_has_prot_file_extension_str_false():
    file_path = "a/path/to/a/file/file.scroop"

    assert has_prot_file_extension(file_path) is False


def test_has_prot_file_extension_path_false():
    file_path = Path("a/path/to/a/file/file.noop")

    assert has_prot_file_extension(file_path) is False


def test_has_prot_file_extension_posix_path_false():
    file_path = PosixPath("a/path/to/a/file/file.loop")

    assert has_prot_file_extension(file_path) is False


def test_has_prot_file_extension_no_extension():
    file_path = "a/path/to/a/file/file"

    assert has_prot_file_extension(file_path) is False

