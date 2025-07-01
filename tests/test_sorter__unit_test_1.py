from __future__ import annotations

import gc
import inspect
import os
import random
import string
import sys
import time
from pathlib import Path
from typing import Any, Callable, Optional

import dill as pickle
import pytest
from app.main import sorter


def codeflash_wrap(
    wrapped: Callable[..., Any],
    test_module_name: str,
    test_class_name: str | None,
    test_name: str,
    function_name: str,
    line_id: str,
    loop_index: int,
    *args: Any,
    **kwargs: Any,
) -> Any:
    test_id = f"{test_module_name}:{test_class_name}:{test_name}:{line_id}:{loop_index}"
    if not hasattr(codeflash_wrap, "index"):
        codeflash_wrap.index = {}
    if test_id in codeflash_wrap.index:
        codeflash_wrap.index[test_id] += 1
    else:
        codeflash_wrap.index[test_id] = 0
    codeflash_test_index = codeflash_wrap.index[test_id]
    invocation_id = f"{line_id}_{codeflash_test_index}"
    test_stdout_tag = f"{test_module_name}:{(test_class_name + '.' if test_class_name else '')}{test_name}:{function_name}:{loop_index}:{invocation_id}"
    print(f"!$######{test_stdout_tag}######$!")
    exception = None
    gc.disable()
    try:
        counter = time.perf_counter_ns()
        return_value = wrapped(*args, **kwargs)
        codeflash_duration = time.perf_counter_ns() - counter
    except Exception as e:
        codeflash_duration = time.perf_counter_ns() - counter
        exception = e
    gc.enable()
    print(f"!######{test_stdout_tag}######!")
    iteration = os.environ["CODEFLASH_TEST_ITERATION"]
    with Path(
        "/tmp/codeflash_cnzaeovl", f"test_return_values_{iteration}.bin"
    ).open("ab") as f:
        pickled_values = (
            pickle.dumps((args, kwargs, exception))
            if exception
            else pickle.dumps((args, kwargs, return_value))
        )
        _test_name = f"{test_module_name}:{(test_class_name + '.' if test_class_name else '')}{test_name}:{function_name}:{line_id}".encode(
            "ascii"
        )
        f.write(len(_test_name).to_bytes(4, byteorder="big"))
        f.write(_test_name)
        f.write(codeflash_duration.to_bytes(8, byteorder="big"))
        f.write(len(pickled_values).to_bytes(4, byteorder="big"))
        f.write(pickled_values)
        f.write(loop_index.to_bytes(8, byteorder="big"))
        f.write(len(invocation_id).to_bytes(4, byteorder="big"))
        f.write(invocation_id.encode("ascii"))
    if exception:
        raise exception
    return return_value


def test_sorter_sorted_list():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1, 2, 3, 4, 5]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_sorted_list",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_reverse_sorted():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [5, 4, 3, 2, 1]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_reverse_sorted",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_unsorted_list():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [3, 1, 4, 5, 2]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_unsorted_list",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_with_duplicates():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [3, 1, 2, 3, 2]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_with_duplicates",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_single_element():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [42]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_single_element",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_two_elements():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [2, 1]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_two_elements",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output
    arr = [1, 2]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_two_elements",
        "sorter",
        "4",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_negative_numbers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [-3, -1, -2, 0, 2]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_negative_numbers",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_mixed_sign_numbers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [5, -2, 0, 3, -1]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_mixed_sign_numbers",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_floats():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [3.1, 2.4, 5.6, 1.0]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_floats",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_mixed_ints_and_floats():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1, 2.2, 0, 3.3, 2]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_mixed_ints_and_floats",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["banana", "apple", "cherry"]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_strings",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_empty_list():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = []
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_empty_list",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_all_identical_elements():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [7, 7, 7, 7, 7]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_all_identical_elements",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_negative_and_positive():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [sys.maxsize, -sys.maxsize - 1, 0, 999999999, -999999999]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_negative_and_positive",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_strings_with_case():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["banana", "Apple", "cherry", "apple"]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_strings_with_case",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_unicode_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["ß", "ä", "ü", "ö", "a"]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_unicode_strings",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_empty_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["", "a", "", "b"]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_empty_strings",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_nested_lists_error():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1, [2, 3], 4]
    with pytest.raises(TypeError):
        _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
        _call__bound__arguments.apply_defaults()
        codeflash_return_value = codeflash_wrap(
            sorter,
            "tests.test_sorter__unit_test_1",
            None,
            "test_sorter_nested_lists_error",
            "sorter",
            "1_0",
            codeflash_loop_index,
            **_call__bound__arguments.arguments,
        )


def test_sorter_mixed_types_error():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1, "a", 2]
    with pytest.raises(TypeError):
        _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
        _call__bound__arguments.apply_defaults()
        codeflash_return_value = codeflash_wrap(
            sorter,
            "tests.test_sorter__unit_test_1",
            None,
            "test_sorter_mixed_types_error",
            "sorter",
            "1_0",
            codeflash_loop_index,
            **_call__bound__arguments.arguments,
        )


def test_sorter_tuple_elements():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [(2, 3), (1, 2), (2, 2), (1, 1)]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_tuple_elements",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_numbers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1e308, 1e-308, -1e308, 0.0]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_numbers",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_nan_and_inf():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [float("inf"), float("-inf"), float("nan"), 0]
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_nan_and_inf",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_random_integers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = random.sample(range(-100000, -99000), 1000)
    expected = sorted(arr)
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_random_integers",
        "sorter",
        "2",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_sorted():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = list(range(1000))
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_sorted",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_reverse_sorted():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = list(range(999, -1, -1))
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_reverse_sorted",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_duplicates():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [random.choice([1, 2, 3, 4, 5]) for _ in range(1000)]
    expected = sorted(arr)
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_duplicates",
        "sorter",
        "2",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["".join(random.choices(string.ascii_letters, k=5)) for _ in range(1000)]
    expected = sorted(arr)
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_strings",
        "sorter",
        "2",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_floats():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [random.uniform(-1000000.0, 1000000.0) for _ in range(1000)]
    expected = sorted(arr)
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_floats",
        "sorter",
        "2",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output


def test_sorter_large_all_identical():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [42] * 1000
    _call__bound__arguments = inspect.signature(sorter).bind(arr.copy())
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_1",
        None,
        "test_sorter_large_all_identical",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    result = codeflash_output
