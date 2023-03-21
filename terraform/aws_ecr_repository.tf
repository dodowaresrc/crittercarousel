resource aws_ecr_repository repo {

    image_tag_mutability = "MUTABLE"
    name                 = local.application_name
    tags                 = merge(local.tags, {name=local.application_name})

    image_scanning_configuration {
        scan_on_push = true
    }
}
