import pytest

from src.fizzbuzz.service_layer import services
from src.fizzbuzz.service_layer.exceptions import CannotCompute


def test_compute_fizzbuzz_with_3_5():
    int1 = 3
    int2 = 5
    limit = 15
    str1 = "fizz"
    str2 = "buzz"

    res = services.compute_fizzbuzz(int1, int2, limit, str1, str2)

    expected = "1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz"
    assert res == expected


def test_compute_fizzbuzz_with_different_string_input():
    int1 = 3
    int2 = 5
    limit = 15
    str1 = "cuir"
    str2 = "moustache"

    res = services.compute_fizzbuzz(int1, int2, limit, str1, str2)

    expected = "1,2,cuir,4,moustache,cuir,7,8,cuir,moustache,11,cuir,13,14,cuirmoustache"
    assert res == expected


def test_compute_fizzbuzz_with_null_limit():
    int1 = 3
    int2 = 5
    limit = 0
    str1 = "fizz"
    str2 = "buzz"

    res = services.compute_fizzbuzz(int1, int2, limit, str1, str2)

    expected = ""
    assert res == expected

