from passprotect.helpers import (
    _derive_key,
    is_locked,
lock_file
)


def test_derive_key():
    salt = b"hello"
    password = "hello_password"
    key = _derive_key(password, salt)

    assert key == b'G3pU8tXRURrW0-75euq3n2zTtQwf2VhbvmjndCg7rrA='


def test_is_locked_unlocked(create_tmp_file_unlocked):
    assert is_locked(create_tmp_file_unlocked) is False


def test_is_locked_locked(create_tmp_file_unlocked):
    # Not good practice using this func to lock the file
    lock_file(create_tmp_file_unlocked, "password", create_tmp_file_unlocked)
    assert is_locked(create_tmp_file_unlocked) is True


def test_file_exists(create_tmp_file_unlocked):
    ...