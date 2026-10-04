# FastAPI Docker Sample with SQLite CRUD

This is a sample project demonstrating a Dockerized FastAPI application with a simple CRUD API backed by SQLite.

## Features
- **FastAPI**: High-performance web framework for building APIs.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Lightweight, file-based database.
- **Docker**: Containerized deployment for consistency.
- **Pytest**: Automated testing for API endpoints.
- **GitHub Actions**: CI pipeline to run tests on every push.

## Quick Start

### 1. Build the Docker image
```bash
docker build -t fastapi-crud-app .
```

### 2. Run the container
```bash
docker run -p 8000:8000 fastapi-crud-app
```
The API will be available at `http://localhost:8000`. You can access the interactive API documentation (Swagger UI) at `http://localhost:8000/docs`.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| POST | `/items/` | Create a new item |
| GET | `/items/` | List all items |
| GET | `/items/{id}` | Get a specific item by ID |
| PUT | `/items/{id}` | Update an existing item |
| DELETE | `/items/{id}` | Delete an item |

## Testing

### Run tests using Docker
```bash
docker run --rm -e PYTHONPATH=. fastapi-crud-app pytest
```

### Run tests locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute pytest:
   ```bash
   pytest
   ```

## CI/CD
This project uses GitHub Actions to automatically run the test suite on every push or pull request to the `main` branch.
