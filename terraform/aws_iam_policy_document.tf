data aws_iam_policy_document assume_role {

    statement {
        effect = "Allow"

        principals {
            type        = "Service"
            identifiers = ["ec2.amazonaws.com"]
        }

        actions = ["sts:AssumeRole"]
    }
}

data aws_iam_policy_document ecr {
    statement {
        sid = join("", [local.deployment_name_title, "EcrPull"])
        effect = "Allow"
        actions = [
            "ecr:BatchCheckLayerAvailability",
            "ecr:GetDownloadUrlForLayer",
            "ecr:GetRepositoryPolicy",
            "ecr:DescribeRepositories",
            "ecr:ListImages",
            "ecr:DescribeImages",
            "ecr:BatchGetImage",
            "ecr:GetLifecyclePolicy",
            "ecr:GetLifecyclePolicyPreview",
            "ecr:ListTagsForResource",
            "ecr:DescribeImageScanFindings"
        ]
        resources = [aws_ecr_repository.repo.arn]
    }

    statement {
        sid       = join("", [local.deployment_name_title, "EcrAuth"])
        effect    = "Allow"
        actions   = ["ecr:GetAuthorizationToken"]
        resources = ["*"]
    }
}
