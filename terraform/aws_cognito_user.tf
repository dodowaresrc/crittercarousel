resource aws_cognito_user cognito_users {
    count         = length(var.user_list)
    user_pool_id  = aws_cognito_user_pool.pool.id
    username      = var.user_list[count.index]
    password      = random_password.cognito_user_passwords[count.index].result
}
