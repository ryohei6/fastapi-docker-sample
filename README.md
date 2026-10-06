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

## ☁️ Deployment to IBM Cloud Code Engine (via Terraform)

You can deploy this application to IBM Cloud Code Engine using the provided Terraform configuration.

### 1. Install Terraform
If you haven't installed Terraform yet, you can do so via binary download:
```bash
# Example for macOS ARM64
curl -L https://releases.hashicorp.com/terraform/1.16.5/terraform_1.16.5_darwin_arm64.zip -o terraform.zip
unzip terraform.zip
mv terraform ~/.local/bin/
```
*(Ensure `~/.local/bin` is in your PATH)*

### 2. Configure Environment Variables
Copy the example environment file and fill in your IBM Cloud credentials and project settings:
```bash
cp .env.example .env
# Edit .env with your API Key and image path
```

### 3. Deploy
Run the following commands from the project root:
```bash
# Load variables
export $(cat .env | xargs)

# Initialize and Apply
terraform init
terraform apply
```

---

## 🛠 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| POST | `/items/` | Create a new item |
| GET | `/items/` | List all items |
| GET | `/items/{id}` | Get a specific item by ID |
| PUT | `/items/{id}` | Update an item |
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
- **Terraform**: Infrastructure as Code for IBM Cloud Code Engine.
- **GitHub Actions**: CI pipeline to run tests on every push.

## CI/CD
This project uses GitHub Actions to automatically run the test suite on every push or pull request to the `main` branch.
