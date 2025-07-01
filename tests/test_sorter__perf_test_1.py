from __future__ import annotations

import gc
import os
import random
import string
import sys
import time
from typing import Any, Callable, Optional

import pytest
from app.main import sorter


def codeflash_wrap(
    wrapped: Callable[..., Any],
    test_module_name: str,
    test_class_name: Optional[str],
    test_name: str,
    function_name: str,
    line_id: str,
    loop_index: int,
    *args: Any,
    **kwargs: Any,
) -> str:
    test_id = f"{test_module_name}:{test_class_name}:{test_name}:{line_id}:{loop_index}"
    if not hasattr(codeflash_wrap, "index"):
        codeflash_wrap.index = {}
    if test_id in codeflash_wrap.index:
        codeflash_wrap.index[test_id] += 1
    else:
        codeflash_wrap.index[test_id] = 0
    codeflash_test_index = codeflash_wrap.index[test_id]
    invocation_id = f"{line_id}_{codeflash_test_index}"
    exception = None
    test_stdout_tag = f"{test_module_name}:{(test_class_name + '.' if test_class_name else '')}{test_name}:{function_name}:{loop_index}:{invocation_id}"
    print(f"!$######{test_stdout_tag}######$!")
    gc.disable()
    try:
        counter = time.perf_counter_ns()
        return_value = wrapped(*args, **kwargs)
        codeflash_duration = time.perf_counter_ns() - counter
    except Exception as e:
        codeflash_duration = time.perf_counter_ns() - counter
        exception = e
    gc.enable()
    print(f"!######{test_stdout_tag}:{codeflash_duration}######!")
    if exception:
        raise exception
    return return_value


def test_sorter_sorted_list():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1, 2, 3, 4, 5]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_sorted_list",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_reverse_sorted():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [5, 4, 3, 2, 1]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_reverse_sorted",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_unsorted_list():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [3, 1, 4, 5, 2]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_unsorted_list",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_with_duplicates():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [3, 1, 2, 3, 2]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_with_duplicates",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_single_element():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [42]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_single_element",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_two_elements():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [2, 1]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_two_elements",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output
    arr = [1, 2]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_two_elements",
        "sorter",
        "4",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_negative_numbers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [-3, -1, -2, 0, 2]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_negative_numbers",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_mixed_sign_numbers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [5, -2, 0, 3, -1]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_mixed_sign_numbers",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_floats():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [3.1, 2.4, 5.6, 1.0]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_floats",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_mixed_ints_and_floats():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1, 2.2, 0, 3.3, 2]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_mixed_ints_and_floats",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["banana", "apple", "cherry"]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_strings",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_empty_list():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = []
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_empty_list",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_all_identical_elements():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [7, 7, 7, 7, 7]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_all_identical_elements",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_negative_and_positive():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [sys.maxsize, -sys.maxsize - 1, 0, 999999999, -999999999]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_negative_and_positive",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_strings_with_case():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["banana", "Apple", "cherry", "apple"]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_strings_with_case",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_unicode_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["ß", "ä", "ü", "ö", "a"]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_unicode_strings",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_empty_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["", "a", "", "b"]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_empty_strings",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_nested_lists_error():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1, [2, 3], 4]
    with pytest.raises(TypeError):
        codeflash_return_value = codeflash_wrap(
            sorter,
            "tests.test_sorter__unit_test_1",
            None,
            "test_sorter_nested_lists_error",
            "sorter",
            "1_0",
            codeflash_loop_index,
            arr.copy(),
        )


def test_sorter_mixed_types_error():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1, "a", 2]
    with pytest.raises(TypeError):
        codeflash_return_value = codeflash_wrap(
            sorter,
            "tests.test_sorter__unit_test_1",
            None,
            "test_sorter_mixed_types_error",
            "sorter",
            "1_0",
            codeflash_loop_index,
            arr.copy(),
        )


def test_sorter_tuple_elements():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [(2, 3), (1, 2), (2, 2), (1, 1)]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_tuple_elements",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_numbers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1e308, 1e-308, -1e308, 0.0]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_numbers",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_nan_and_inf():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [float("inf"), float("-inf"), float("nan"), 0]
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_nan_and_inf",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_random_integers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = random.sample(range(-100000, -99000), 1000)
    expected = sorted(arr)
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_random_integers",
        "sorter",
        "2",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_sorted():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = list(range(1000))
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_sorted",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_reverse_sorted():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = list(range(999, -1, -1))
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_reverse_sorted",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_duplicates():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [random.choice([1, 2, 3, 4, 5]) for _ in range(1000)]
    expected = sorted(arr)
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_duplicates",
        "sorter",
        "2",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["".join(random.choices(string.ascii_letters, k=5)) for _ in range(1000)]
    expected = sorted(arr)
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_strings",
        "sorter",
        "2",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_floats():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [random.uniform(-1000000.0, 1000000.0) for _ in range(1000)]
    expected = sorted(arr)
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_floats",
        "sorter",
        "2",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_all_identical():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [42] * 1000
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_all_identical",
        "sorter",
        "1",
        codeflash_loop_index,
        arr.copy(),
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output
