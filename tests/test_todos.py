from fastapi.testclient import TestClient
from main import app
from firebase_admin import auth
import pytest

client = TestClient(app)


# Test Get all todos being authentified
def test_get_todos_success(auth_user):
  res = client.get("/todos", headers={
    "Authorization": f"Bearer {auth_user['access_token']}"
  })
  assert res.status_code == 200

# Test Get all todos error while unauthentified (401 = UNAUTHORIZED)
def test_get_todos_unauthorized_if_not_authentified():
  res = client.get("/todos")
  assert res.status_code == 401


# Test post todos success being auth
def test_post_todos_success(auth_user):
  res = client.post("/todos", json={"title": "Test todo", "description": "fghjkljhgfghj"}, headers={"Authorization": f"Bearer {auth_user['access_token']}"})
  assert res.status_code == 201 



# Test create todos error
def test_post_todos_unauthorized_if_not_athentified():
  res = client.post("/todos", json={
  "title": "RDV medecin",
  "description": "fdfghsjkds"
})
  assert res.status_code == 401