resource aws_s3_bucket_acl acl {
    acl    = "private"
    bucket = aws_s3_bucket.bucket.id
}
