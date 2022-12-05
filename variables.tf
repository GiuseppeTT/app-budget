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
  description = "Database administrator username"
  sensitive   = true
}

variable "database_password" {
  type        = string
  description = "Database administrator password"
  sensitive   = true
}
