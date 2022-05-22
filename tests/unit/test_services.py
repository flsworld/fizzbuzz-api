from src.fizzbuzz.service_layer import services


def test_compute_fizzbuzz():
    int1 = 3
    int2 = 5
    limit = 15
    str1 = "fizz"
    str2 = "buzz"

    res = services.compute_fizzbuzz(int1, int2, limit, str1, str2)

    expected = "1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz"
    assert res == expected
