resource aws_iam_role role {
    name               = local.deployment_name
    assume_role_policy = data.aws_iam_policy_document.assume_role.json

    managed_policy_arns = [
        data.aws_iam_policy.web_tier.arn,
        data.aws_iam_policy.multi_container.arn,
        aws_iam_policy.ecr.arn,
        aws_iam_policy.dynamodb.arn
    ]
}
