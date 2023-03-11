resource random_password dbadmin {
    length      = 32
    min_lower   = 4
    min_numeric = 4
    min_upper   = 4
    special     = false
}
