data template_file ebe_settings {
    template = file("${path.module}/ebe_settings.json")
    vars = {
        app_deployment   = local.deployment_name
        app_region       = local.tags.region
        rds_hostname     = aws_db_instance.postgres.address
        rds_port         = aws_db_instance.postgres.port
        rds_db_name      = aws_db_instance.postgres.db_name
        rds_username     = aws_db_instance.postgres.username
        rds_password     = random_password.dbadmin.result
        instance_profile = aws_iam_instance_profile.profile.name
        security_group   = aws_security_group.vm.id
        subnet0          = aws_subnet.subnet0.id
        subnet1          = aws_subnet.subnet1.id
        vpc              = aws_vpc.vpc.id
    }
}
