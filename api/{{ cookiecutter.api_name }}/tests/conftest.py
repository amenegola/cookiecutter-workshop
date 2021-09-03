import pytest
import json
from api.controller import app
from fastapi.testclient import TestClient


@pytest.fixture
def model_payload_post():
    payload = {
        "age": 90,
        "gender": "M",
        "openAnswer": "dor de cabeca"
    }
    return payload

@pytest.fixture
def wrong_payload_post():
    payload = {
        "age": "teste",
        "gender": "M",
        "openAnswer": "dor de cabeca"
    }
    return payload


@pytest.fixture
def fast_test_client():
    with TestClient(app) as test_client:
        yield test_client
