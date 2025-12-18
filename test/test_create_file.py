from pypassword_protect.source.encryption_decryption import create_file


def test_create_file(tmp_files, teardown_delete_tmp_files):
    test_file = str(tmp_files.joinpath("test_create_file.prot"))

    file_path = create_file(test_file)
    assert test_file[-42:] == "/test/tmp_test_files/test_create_file.prot"
