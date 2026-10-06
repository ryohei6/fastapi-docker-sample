variable "ibm_cloud_api_key" {
  type      = string
  sensitive = true
  description = "IBM Cloud API Key"
}

variable "ibm_cloud_region" {
  type        = string
  default     = "us-south"
  description = "IBM Cloud region"
}

variable "ce_project_name" {
  type        = string
  description = "Name of the Code Engine project"
}

variable "ce_app_name" {
  type        = string
  description = "Name of the Code Engine application"
}

variable "ce_image" {
  type        = string
  description = "Container image to deploy (e.g., icr.io/namespace/image:tag)"
}
