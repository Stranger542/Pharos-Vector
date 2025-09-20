variable "aws_region" {
  description = "AWS Region"
  default     = "us-west-2"
}

variable "vpc_cidr" {
  description = "VPC CIDR Block"
  default     = "10.0.0.0/16"
}

variable "db_name" {
  description = "Postgres DB name"
  default     = "fakenewsdb"
}

variable "db_username" {
  description = "Postgres username"
  default     = "postgres"
}

variable "db_password" {
  description = "Postgres password"
  sensitive   = true
}
