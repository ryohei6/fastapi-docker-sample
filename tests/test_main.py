from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db

# Use a separate in-memory SQLite DB for tests
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_temp.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "description": "Test Description"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert "id" in data

def test_read_items():
    # First create one
    client.post("/items/", json={"name": "Read Item", "description": "Read Desc"})
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_read_item():
    # Create one
    res = client.post("/items/", json={"name": "Single Item", "description": "Single Desc"})
    item_id = res.json()["id"]
    
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Single Item"

def test_update_item():
    res = client.post("/items/", json={"name": "Update Me", "description": "Old Desc"})
    item_id = res.json()["id"]
    
    response = client.put(f"/items/{item_id}", json={"name": "Updated", "description": "New Desc"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated"

def test_delete_item():
    res = client.post("/items/", json={"name": "Delete Me", "description": "Delete Desc"})
    item_id = res.json()["id"]
    
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    
    # Verify it's gone
    get_res = client.get(f"/items/{item_id}")
    assert get_res.status_code == 404
