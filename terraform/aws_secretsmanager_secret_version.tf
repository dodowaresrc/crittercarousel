resource aws_secretsmanager_secret_version dbadmin {
    secret_id     = aws_secretsmanager_secret.dbadmin.id
    secret_string = random_password.dbadmin.result
}

resource aws_secretsmanager_secret_version users {
    count         = length(var.user_list)
    secret_id     = aws_secretsmanager_secret.secret_list[count.index].id
    secret_string = random_password.cognito_user_passwords[count.index].result
}

resource aws_secretsmanager_secret_version cognitoclient {
    secret_id     = aws_secretsmanager_secret.cognitoclient.id
    secret_string = aws_cognito_user_pool_client.client.client_secret
}