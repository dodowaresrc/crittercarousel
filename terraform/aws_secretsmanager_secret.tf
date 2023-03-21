resource aws_secretsmanager_secret dbadmin {
    name = "${local.deployment_name}-dbadmin"
    tags = merge(local.tags, {username="dbadmin"})
}

resource aws_secretsmanager_secret secret_list {
    count = length(var.user_list)
    name  = local.secret_names[count.index]
    tags  = merge(local.tags, {username=var.user_list[count.index]})
}

resource aws_secretsmanager_secret cognitoclient {
    name  = "${local.deployment_name}-cognitoclient"
    tags  = merge(local.tags, {username="cognitoclient"})
}
