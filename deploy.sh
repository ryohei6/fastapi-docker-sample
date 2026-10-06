#!/bin/bash
set -e

# 1. Load environment variables from .env
if [ ! -f .env ]; then
    echo "Error: .env file not found. Please create it from .env.example"
    exit 1
fi
export $(grep -v '^#' .env | xargs)

echo "🚀 Starting deployment process..."

# 2. Build Docker Image
echo "📦 Building Docker image: $TF_VAR_ce_image..."
docker build -t $TF_VAR_ce_image .

# 3. Push to IBM Cloud Container Registry
echo "📤 Pushing image to ICR..."
# Note: This assumes you have already run 'ibmcloud cr login'
docker push $TF_VAR_ce_image

# 4. Terraform Deployment
echo "🏗️ Applying Terraform configuration..."
terraform init
terraform apply -auto-approve

echo "✅ Deployment complete!"
