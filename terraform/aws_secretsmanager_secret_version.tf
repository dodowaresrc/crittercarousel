resource aws_secretsmanager_secret_version dbadmin {
    secret_id     = aws_secretsmanager_secret.dbadmin.id
    secret_string = random_password.dbadmin.result
}
