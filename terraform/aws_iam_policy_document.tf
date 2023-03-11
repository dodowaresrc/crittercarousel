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

data aws_iam_policy_document dynamodb {
    statement {
        sid = join("", [local.deployment_name_title, "DynamoTables"])
        effect = "Allow"
        actions = [
            "dynamodb:BatchGet*",
            "dynamodb:DescribeStream",
            "dynamodb:DescribeTable",
            "dynamodb:Get*",
            "dynamodb:Query",
            "dynamodb:Scan",
            "dynamodb:BatchWrite*",
            "dynamodb:Delete*",
            "dynamodb:Update*",
            "dynamodb:PutItem"
        ]
        resources = [
            aws_dynamodb_table.critters.arn,
            aws_dynamodb_table.events.arn,
            aws_dynamodb_table.species.arn
        ]
    }
}
