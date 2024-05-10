from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

def test_create_user_success():
    res = client.post("/auth/signup", json={
        "email": "test.user122@gmail.com" , "password": "password"
    })
    assert res.status_code == 201 


def test_create_user_conflict(create_user):
    res = client.post("/auth/signup", json={
        "email": "test.user122@gmail.com", 'password': "password"
    })
    assert res.status_code == 409