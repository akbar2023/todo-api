from firebase_admin import auth
from fastapi.testclient import TestClient
from main import app
import pytest

import os

os.environ['TESTING'] = 'True'

client = TestClient(app)

@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    #Nettoyer le directory une fois fini
    def remove_test_users():
        users = auth.list_users().iterate_all()
        for user in users:
            if user.email.startswith("test."):
                auth.delete_user(user.uid)
    request.addfinalizer(remove_test_users)

@pytest.fixture
def create_user():
    user_credential = client.post("/auth/signup", json={
        "email": "test.user2@gmail.com", 'password': "password"
    })


@pytest.fixture()
def auth_user(create_user):
    user_credential = client.post("/auth/login", data={
        "username": "test.user2@gmail.com", 'password': "password"
    })
    return user_credential.json()