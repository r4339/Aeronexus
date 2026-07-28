variable "aws_region" {

  description = "AWS Region"

  type = string

}

variable "project_name" {

  description = "Project Name"

  type = string

}

variable "environment" {

  description = "Environment"

  type = string

}
variable "instance_type" {
  type    = string
  default = "t2.micro"
}

variable "key_name" {
  type = string
}
variable "db_name" {
  default = "aeronexus"
}

variable "db_username" {
  default = "postgres"
}

variable "db_password" {
  description = "Database Password"
  type        = string
  sensitive   = true
}