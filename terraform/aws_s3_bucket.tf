resource aws_s3_bucket bucket {
    bucket = local.application_name
    tags   = merge(local.tags, {name=local.application_name})
}
