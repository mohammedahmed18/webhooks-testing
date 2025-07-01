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


def test_sorter_basic_sorted():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1, 2, 3, 4, 5]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_basic_sorted",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_basic_reverse():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [5, 4, 3, 2, 1]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_basic_reverse",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_basic_unsorted():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [3, 1, 4, 5, 2]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_basic_unsorted",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_basic_duplicates():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [2, 3, 2, 1, 3]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_basic_duplicates",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_basic_negative_numbers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [-3, -1, -2, 0, 2, 1]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_basic_negative_numbers",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_basic_floats():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1.5, 2.3, 0.7, 1.5]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_basic_floats",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_basic_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["banana", "apple", "cherry"]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_basic_strings",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_basic_mixed_case_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["Banana", "apple", "Cherry"]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_basic_mixed_case_strings",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_basic_single_element():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [42]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_basic_single_element",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_basic_two_elements():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [2, 1]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_basic_two_elements",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_basic_all_equal():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [7, 7, 7, 7]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_basic_all_equal",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_edge_empty():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = []
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_edge_empty",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_edge_large_integers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [sys.maxsize, -sys.maxsize - 1, 0]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_edge_large_integers",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_edge_large_floats():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [1e308, -1e308, 0.0]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_edge_large_floats",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_edge_strings_with_numbers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["10", "2", "1"]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_edge_strings_with_numbers",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_edge_unicode_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["éclair", "apple", "Éclair", "banana"]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_edge_unicode_strings",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_edge_mutation():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [3, 1, 2]
    arr_copy = arr[:]
    _call__bound__arguments = inspect.signature(sorter).bind(arr_copy)
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_edge_mutation",
        "sorter",
        "2",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )


def test_sorter_edge_boolean_values():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [True, False, True]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_edge_boolean_values",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_edge_objects():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])

    class Dummy:

        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            return self.value < other.value

        def __eq__(self, other):
            return self.value == other.value

        def __repr__(self):
            return f"Dummy({self.value})"

    arr = [Dummy(3), Dummy(1), Dummy(2)]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_edge_objects",
        "sorter",
        "2",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    sorted_arr = codeflash_output


def test_sorter_edge_already_sorted_large():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = list(range(1000))
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_edge_already_sorted_large",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_edge_reverse_sorted_large():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = list(range(999, -1, -1))
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_edge_reverse_sorted_large",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_edge_stability():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])

    class StableObj:

        def __init__(self, key, id):
            self.key = key
            self.id = id

        def __lt__(self, other):
            return self.key < other.key

        def __eq__(self, other):
            return self.key == other.key and self.id == other.id

        def __repr__(self):
            return f"StableObj({self.key}, {self.id})"

    arr = [StableObj(1, "a"), StableObj(1, "b"), StableObj(2, "c")]
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_edge_stability",
        "sorter",
        "2",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
    sorted_arr = codeflash_output


def test_sorter_large_random_integers():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = random.sample(range(-10000, -9000), 1000)
    expected = sorted(arr)
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_large_random_integers",
        "sorter",
        "2",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_large_random_floats():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [random.uniform(-1000000.0, 1000000.0) for _ in range(1000)]
    expected = sorted(arr)
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_large_random_floats",
        "sorter",
        "2",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_large_duplicates():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = [random.choice([1, 2, 3, 4, 5]) for _ in range(1000)]
    expected = sorted(arr)
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_large_duplicates",
        "sorter",
        "2",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_large_strings():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = ["".join(random.choices(string.ascii_letters, k=5)) for _ in range(1000)]
    expected = sorted(arr)
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_large_strings",
        "sorter",
        "2",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_large_already_sorted():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = list(range(1000))
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_large_already_sorted",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value


def test_sorter_large_reverse_sorted():
    random.seed(42)
    codeflash_loop_index = int(os.environ["CODEFLASH_LOOP_INDEX"])
    arr = list(range(999, -1, -1))
    _call__bound__arguments = inspect.signature(sorter).bind(arr[:])
    _call__bound__arguments.apply_defaults()
    codeflash_return_value = codeflash_wrap(
        sorter,
        "tests.test_sorter__unit_test_0",
        None,
        "test_sorter_large_reverse_sorted",
        "sorter",
        "1",
        codeflash_loop_index,
        **_call__bound__arguments.arguments,
    )
    codeflash_output = codeflash_return_value
