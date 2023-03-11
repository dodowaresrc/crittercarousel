resource aws_elastic_beanstalk_application app {
    name = local.deployment_name
    tags = merge(local.tags, {name=local.deployment_name})
}
