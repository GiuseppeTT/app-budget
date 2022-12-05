terraform {
  required_version = "~> 1.3"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.33"
    }
  }

  cloud {
    organization = "giutt-org"
    workspaces {
      name = "test-app-budget-terraform-cloud-workspace"
    }
  }
}
