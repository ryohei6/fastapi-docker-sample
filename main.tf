terraform {
  required_providers {
    ibm = {
      source  = "IBM/ibm"
      version = "~> 1.70.0"
    }
  }
}

provider "ibm" {
  region = var.ibm_cloud_region
}

# Code Engine Project
resource "ibm_cloud_ce_project" "project" {
  name = var.ce_project_name
}

# Code Engine App
resource "ibm_cloud_ce_app" "app" {
  name       = var.ce_app_name
  project_id = ibm_cloud_ce_project.project.id

  image {
    registry = var.ce_image
  }

  resource_limit {
    cpu    = "0.25"
    memory = "0.25G"
  }

  visibility = "PUBLIC"
}

output "app_url" {
  value = ibm_cloud_ce_app.app.url
}
