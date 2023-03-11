data aws_iam_policy web_tier {
    arn = "arn:aws:iam::aws:policy/AWSElasticBeanstalkWebTier"   
}

data aws_iam_policy multi_container {
    arn = "arn:aws:iam::aws:policy/AWSElasticBeanstalkMulticontainerDocker"   
}

resource aws_iam_policy ecr {
    name   = "${local.deployment_name}-ecr"
    policy = data.aws_iam_policy_document.ecr.json
}

resource aws_iam_policy dynamodb {
    name   = "${local.deployment_name}-dynamodb"
    policy = data.aws_iam_policy_document.dynamodb.json
}
