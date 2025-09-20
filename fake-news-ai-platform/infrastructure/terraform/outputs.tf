output "cluster_endpoint" {
  description = "EKS cluster endpoint"
  value       = aws_eks_cluster.main.endpoint
}

output "db_instance_endpoint" {
  description = "Postgres instance endpoint"
  value       = aws_db_instance.postgres.endpoint
}
