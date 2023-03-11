resource aws_secretsmanager_secret dbadmin {
    name = "${local.deployment_name}-dbadmin"
}
