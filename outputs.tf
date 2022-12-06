output "api_docs" {
  description = "The API docs as accessed from the container's FQND"
  value       = "${azurerm_container_group.this.fqdn}/docs"
}
