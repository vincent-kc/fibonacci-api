import json
import pytest

from fastapi.testclient import TestClient


from app.main import app, compute_fibonacci


client = TestClient(app)


def test_fibonacci_ok():
    response = client.post("/fibonacci", json.dumps({"n": 5}))
    assert response.status_code == 200
    assert "nth" in response.json().keys()
    assert "status" in response.json().keys()


def test_fibonacci_invalid_input():
    response = client.post("/fibonacci", json.dumps({"n": "nn5"}))
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"


def test_fibonacci_valid_int_str_type():
    response = client.post("/fibonacci", json.dumps({"n": "5"}))
    assert response.status_code == 200
    assert "nth" in response.json().keys()
    assert "status" in response.json().keys()


@pytest.mark.parametrize(
    "test_input,expected", [(7, 8), (5, 3), (21, 6765), (13, 144), (41, 102334155)]
)
def test_compute_fibonacci(test_input, expected):
    nth = compute_fibonacci(test_input)
    assert nth == expected
