from passprotect.helpers import _derive_key, file_exists, is_locked, lock_file


def test_derive_key():
    salt = b"hello"
    password = "hello_password"
    key = _derive_key(password, salt)

    assert key == b"G3pU8tXRURrW0-75euq3n2zTtQwf2VhbvmjndCg7rrA="


def test_is_locked_unlocked(create_tmp_file_unlocked, teardown_delete_tmp_files):
    assert is_locked(create_tmp_file_unlocked) is False


def test_is_locked_locked(create_tmp_file_unlocked, teardown_delete_tmp_files):
    # Not good practice using this func to lock the file
    lock_file(create_tmp_file_unlocked, "password", create_tmp_file_unlocked)
    assert is_locked(create_tmp_file_unlocked) is True


def test_file_exists_true(create_tmp_file_unlocked, teardown_delete_tmp_files):
    assert file_exists(create_tmp_file_unlocked) is True


def test_file_exists_false(tmp_files):
    assert file_exists(tmp_files.joinpath("file.txt")) is False
