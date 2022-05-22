from fastapi.testclient import TestClient

from src.fizzbuzz import app

client = TestClient(app)


def test_read_main():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_compute_string_like_fizzbuzz():
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
