from importlib.resources import files

from passprotect.helpers import lock_file, unlock_file


def test_lock_file(create_tmp_file_unlocked):
    file_path = str(
        files("test.tmp_test_files").joinpath("tmp_file_unlocked.unlocked")
    )
    with open(file_path, "w") as open_file:
        open_file.write("yes no, maybe, I don't know, can you repeat the question")

    lock_file(file_path, "password")
    print()


def test_unlock_file(create_tmp_file_unlocked):
    file_path = str(
        files("test.tmp_test_files").joinpath("tmp_file_locked")
    )
    with open(file_path, "w") as open_file:
        open_file.write("yes no, maybe, I don't know, can you repeat the question")

    lock_file(file_path, "password")
    print()
    output_location = str(
        files("test.tmp_test_files").joinpath("tmp_file_locked")
    )
    unlock_file(file_path, "password", output_location)
