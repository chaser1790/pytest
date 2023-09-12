from utils import arrs


def test_get_existing_index():
    assert arrs.get([1, 2, 3, 4], 2) == 3  # Тестирование существующего индекса

def test_get_default_value():
    assert arrs.get([1, 2, 3], 5, "default") == "default"  # Тестирование несуществующего индекса с значением по умолчанию


def test_slice_negative_indexes():
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]  # Тестирование отрицательных индексов

def test_slice_end_exceeds_length():
    assert arrs.my_slice([1, 2, 3, 4, 5], end=10) == [1, 2, 3, 4, 5]  # Тестирование превышения конечного индекса

def test_slice_start_and_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]  # Тестирование указания начала и конца среза

def test_slice_empty_coll():
    assert arrs.my_slice([], 0, 1) == []  # Тестирование пустого списка

def test_slice_no_start_or_end():
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  # Тестирование отсутствия указания начала и конца среза