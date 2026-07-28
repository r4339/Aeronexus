resource "aws_s3_bucket" "media" {

  bucket = "${lower(var.project_name)}-${var.environment}-media"

  tags = {
    Name = "${var.project_name} Media"
  }

}
resource "aws_s3_bucket_versioning" "media_versioning" {

  bucket = aws_s3_bucket.media.id

  versioning_configuration {

    status = "Enabled"

  }

}
resource "aws_s3_bucket_public_access_block" "media" {

  bucket = aws_s3_bucket.media.id

  block_public_acls  = true
  ignore_public_acls = true

  block_public_policy     = true
  restrict_public_buckets = true

}
resource "aws_s3_bucket_server_side_encryption_configuration" "media" {

  bucket = aws_s3_bucket.media.id

  rule {

    apply_server_side_encryption_by_default {

      sse_algorithm = "AES256"

    }

  }

}