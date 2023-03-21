resource aws_s3_object dockercompose {
    bucket  = aws_s3_bucket.bucket.id
    key     = "${local.application_name}/${var.application_version}/docker-compose.yml"
    content = jsonencode(local.docker_compose_data)
}
