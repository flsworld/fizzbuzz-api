from fastapi.testclient import TestClient

from src.fizzbuzz import app

client = TestClient(app)


def test_read_main():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_compute_string_like_fizzbuzz(cache):
    body = {
        "int1": 3,
        "int2": 5,
        "limit": 15,
        "str1": "fizz",
        "str2": "buzz",
    }

    response = client.post("/api/compute", json=body)

    assert response.status_code == 200
    assert response.json() == {
        "computed_string": "1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz"
    }


def test_compute_string_like_fizzbuzz_when_int_inputs_are_identical(cache):
    body = {
        "int1": 3,
        "int2": 3,
        "limit": 15,
        "str1": "fizz",
        "str2": "buzz",
    }

    response = client.post("/api/compute", json=body)

    assert response.status_code == 400
    assert response.json() == {"error": "'Multiple of' inputs are identical"}


def test_compute_string_like_fizzbuzz_when_zero_in_inputs(cache):
    body = {
        "int1": 3,
        "int2": 0,
        "limit": 15,
        "str1": "fizz",
        "str2": "buzz",
    }

    response = client.post("/api/compute", json=body)

    assert response.status_code == 400
    assert response.json() == {"error": "'Multiple of' zero as input is not possible"}


def test_popular_request(cache):
    body = {
        "int1": 3,
        "int2": 5,
        "limit": 15,
        "str1": "fizz",
        "str2": "buzz",
    }
    client.post("/api/compute", json=body)
    client.post("/api/compute", json=body)
    client.post("/api/compute", json=body)

    response = client.get("api/popular-request")

    assert response.status_code == 200
    expected = {**body, "number_of_hit": 3}
    assert response.json() == expected


def test_popular_request_when_no_request_made_yet():

    response = client.get("api/popular-request")

    assert response.status_code == 200
    assert response.json() == {"warning": "No request made yet"}
