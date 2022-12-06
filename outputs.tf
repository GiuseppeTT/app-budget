output "database_fqdn" {
  description = "The database FQND"
  value       = azurerm_postgresql_flexible_server.this.fqdn
}


output "api_docs" {
  description = "The API docs as accessed from the container's FQND"
  value       = "${azurerm_container_group.this.fqdn}/docs"
}
