from urllib import response
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200


def test_auth_fail():
    response = client.post("/auth/token", data={"username": "", "password": ""})

    assert response.status_code == 422
    assert response.json().get("access_token") is None
    assert response.json().get("detail")[0]["msg"] == "field required"


def test_auth_success():
    response = client.post("/auth/token", data={"username": "taha", "password": "taha"})
    assert response.status_code == 200
    access_token = response.json().get("access_token")
    assert access_token


def test_create_article():
    response = client.post(
        "/article/",
        json={
            "title": "This is a new title",
            "content": "content is a new one",
            "published": True,
            "creator_id": 1,
        },
    )

    assert response.status_code == 200
    assert response.json().get("title") == "This is a new title"


def test_get_article():
    response = client.post("/auth/token", data={"username": "taha", "password": "taha"})
    assert response.status_code == 200
    access_token = response.json().get("access_token")
    assert access_token
    
    response = client.get('/article/1', headers={'Authorization': f'bearer {access_token}'})
    assert response.status_code == 200