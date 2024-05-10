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






# Test patch todos success being auth
def test_patch_todos_success(auth_user):
    # Créer un todo pour mettre à jour
    res_create = client.post("/todos", json={"title": "Test todo", "description": "fghjkljhgfghj"}, headers={"Authorization": f"Bearer {auth_user['access_token']}"})
    assert res_create.status_code == 201
    todo_id = res_create.json()["id"]

    # Mettre à jour le todo
    updated_data = {"title": "Updated todo", "description": "Updated description"}
    res_patch = client.patch(f"/todos/{todo_id}", json=updated_data, headers={"Authorization": f"Bearer {auth_user['access_token']}"})
    
    # Vérifier le statut de la réponse
    assert res_patch.status_code == 204

    # Vérifier que le todo a été mis à jour
    res_get = client.get(f"/todos/{todo_id}", headers={"Authorization": f"Bearer {auth_user['access_token']}"})
    assert res_get.status_code == 200
    assert res_get.json()["title"] == updated_data["title"]
    assert res_get.json()["description"] == updated_data["description"]



# Test delete todos success being auth
def test_delete_todos_success(auth_user):
    # Créer un todo à supprimer
    res_create = client.post("/todos", json={"title": "Test todo", "description": "fghjkljhgfghj"}, headers={"Authorization": f"Bearer {auth_user['access_token']}"})
    assert res_create.status_code == 201
    todo_id = res_create.json()["id"]

    # Supprimer le todo
    res_delete = client.delete(f"/todos/{todo_id}", headers={"Authorization": f"Bearer {auth_user['access_token']}"})
    
    # Vérifier le statut de la réponse
    assert res_delete.status_code == 204

    # Vérifier que le todo a été supprimé en essayant de le récupérer
    res_get = client.get(f"/todos/{todo_id}", headers={"Authorization": f"Bearer {auth_user['access_token']}"})
    assert res_get.status_code == 404  # On s'attend à ce que le todo soit introuvable


