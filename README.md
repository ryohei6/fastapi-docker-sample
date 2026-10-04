# FastAPI Docker Sample with SQLite CRUD

This is a sample project demonstrating a Dockerized FastAPI application with a simple CRUD API backed by SQLite.

## 🚀 Quick Start

### ⚠️ Important: Build Before Running
Before you can run the application or the tests, you **must** build the Docker image. If you get an error like `Unable to find image... locally` or `repository does not exist`, it means you skipped this step.

#### 1. Build the Docker image
Run this command from the project root:
```bash
docker build -t fastapi-crud-app .
```

#### 2. Run the container
Once the build is finished, start the app:
```bash
docker run -p 8000:8000 fastapi-crud-app
```
The API will be available at `http://localhost:8000`. You can access the interactive API documentation (Swagger UI) at `http://localhost:8000/docs`.

---

## 🛠 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| POST | `/items/` | Create a new item |
| GET | `/items/` | List all items |
| GET | `/items/{id}` | Get a specific item by ID |
| PUT | `/items/{id}` | Update an existing item |
| DELETE | `/items/{id}` | Delete an item |

---

## 🧪 Testing

### Run tests using Docker
**Note:** Ensure you have built the image using `docker build -t fastapi-crud-app .` first.

```bash
docker run --rm -e PYTHONPATH=. fastapi-crud-app pytest
```

### Run tests locally (without Docker)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute pytest:
   ```bash
   pytest
   ```

---

## ⚙️ Technical Details
- **FastAPI**: High-performance web framework.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Lightweight, file-based database (auto-generated as `test.db` on startup).
- **Docker**: Containerized deployment.
- **GitHub Actions**: CI pipeline to run tests on every push.

## CI/CD
This project uses GitHub Actions to automatically run the test suite on every push or pull request to the `main` branch.
