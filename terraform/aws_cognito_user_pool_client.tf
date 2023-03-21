resource aws_cognito_user_pool_client client {
    name                                 = local.deployment_name
    user_pool_id                         = aws_cognito_user_pool.pool.id
    explicit_auth_flows                  = ["USER_PASSWORD_AUTH"]
    allowed_oauth_flows_user_pool_client = false
    supported_identity_providers         = ["COGNITO"]
    generate_secret                      = true
}
