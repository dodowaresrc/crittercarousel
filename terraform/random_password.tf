resource random_password dbadmin {
    length      = 32
    min_lower   = 4
    min_numeric = 4
    min_upper   = 4
    special     = false
}

resource random_password cognito_user_passwords {
    count       = length(var.user_list)
    length      = 32
    min_lower   = 4
    min_numeric = 4
    min_upper   = 4
    special     = false
}
