from passprotect.helpers import is_locked, lock_file, unlock_file


def test_lock_file(create_tmp_file_unlocked, teardown_delete_tmp_files):
    with open(create_tmp_file_unlocked, "w") as open_file:
        open_file.write("yes no, maybe, I don't know, can you repeat the question")

    lock_file(create_tmp_file_unlocked, "password", create_tmp_file_unlocked)

    assert is_locked(create_tmp_file_unlocked) is True


def test_unlock_file(create_tmp_file_unlocked, teardown_delete_tmp_files):
    with open(create_tmp_file_unlocked, "w") as open_file:
        open_file.write("yes no, maybe, I don't know, can you repeat the question")

    lock_file(create_tmp_file_unlocked, "password", create_tmp_file_unlocked)
    unlock_file(create_tmp_file_unlocked, "password", create_tmp_file_unlocked)
    assert is_locked(create_tmp_file_unlocked) is False
