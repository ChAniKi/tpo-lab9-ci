
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def test_get_user():
    response = requests.get(
        f"{BASE_URL}/users/1",
        timeout=TIMEOUT
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert data["id"] == 1
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)
    assert "@" in data["email"]
    assert "address" in data


def test_create_user():
    payload = {
        "name": "Alex Test",
        "username": "alextest",
        "email": "alex.test@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload,
        timeout=TIMEOUT
    )

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert isinstance(data["id"], int)
    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]


def test_update_user():
    payload = {
        "id": 1,
        "name": "Alex Updated",
        "username": "alexupdated",
        "email": "alex.updated@example.com"
    }

    response = requests.put(
        f"{BASE_URL}/users/1",
        json=payload,
        timeout=TIMEOUT
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]
