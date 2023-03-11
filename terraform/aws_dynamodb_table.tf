resource aws_dynamodb_table critters {

    name = "${local.deployment_name}-critters"

    attribute {
        name = "name"
        type = "S"
    }

    attribute {
        name = "species"
        type = "S"
    }

    hash_key = "name"

    range_key = "species"

    billing_mode = "PAY_PER_REQUEST"

    tags = local.tags
}

resource aws_dynamodb_table species {

    name = "${local.deployment_name}-species"

    attribute {
        name = "name"
        type = "S"
    }

    hash_key = "name"

    billing_mode = "PAY_PER_REQUEST"

    tags = local.tags
}

resource aws_dynamodb_table events {

    name = "${local.deployment_name}-events"

    attribute {
        name = "id"
        type = "S"
    }

    hash_key = "id"

    billing_mode = "PAY_PER_REQUEST"

    tags = local.tags
}
