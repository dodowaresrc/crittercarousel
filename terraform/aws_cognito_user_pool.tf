resource aws_cognito_user_pool pool {

    name = local.deployment_name

    account_recovery_setting {
        recovery_mechanism {
            name     = "verified_email"
            priority = 1
        }
    }

    password_policy {
        minimum_length    = 20
        require_lowercase = true
        require_numbers   = true
        require_symbols   = false
        require_uppercase = true
    }

    tags = local.tags
}    
