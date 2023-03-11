resource aws_elastic_beanstalk_application_version version {
    application = aws_elastic_beanstalk_application.app.name
    bucket      = aws_s3_bucket.bucket.id
    key         = aws_s3_object.dockercompose.id
    name        = var.application_version
}
