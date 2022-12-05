variable "prefix" {
  default     = "app-budget"
  type        = string
  description = "The prefix used for all resources"
}

variable "location" {
  default     = "east us"
  type        = string
  description = "The Azure location used for all resources"
}

variable "database_username" {
  type        = string
  description = "The database administrator username"
  sensitive   = true
}

variable "database_password" {
  type        = string
  description = "The database administrator password"
  sensitive   = true
}

variable "project_repository_url" {
  default     = "https://github.com/GiuseppeTT/app-budget"
  type        = string
  description = "The project's repository URL"
}

variable "project_repository_token" {
  default     = "fake-repository-is-public"
  type        = string
  description = "The project's repository token"
  sensitive   = true
}

variable "docker_image_tag" {
  default     = "latest"
  type        = string
  description = "The docker image's tag"
}
