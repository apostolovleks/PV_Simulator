from conftest import test_file_name, test_result_data, test_disk_repository


def test_write_to_file():
    test_disk_repository._write_file(test_result_data)

    assert test_file_name.stat().st_size > 0
    open(test_file_name, 'w').close()


def test_add_to_file():
    size_before_test = test_file_name.stat().st_size
    test_disk_repository._add_to_file(test_result_data)
    size_after_test = test_file_name.stat().st_size

    assert size_before_test < size_after_test
    open(test_file_name, 'w').close()


def test_save_to_scv():
    test_file_name.unlink()
    test_disk_repository.save_to_csv(test_result_data)

    assert test_file_name.exists()
    assert test_file_name.stat().st_size > 0
    open(test_file_name, 'w').close()
