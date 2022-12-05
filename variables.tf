variable "prefix" {
  description = "The prefix used for all resources"
  type        = string
  default     = "test-app-budget"
}

variable "location" {
  description = "The Azure location used for all resources"
  type        = string
  default     = "east us"
}

variable "database_username" {
  description = "Database administrator username"
  type        = string
  sensitive   = true
}

variable "database_password" {
  description = "Database administrator password"
  type        = string
  sensitive   = true
}
