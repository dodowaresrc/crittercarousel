data template_file ebe_common_settings {
    template = file("${path.module}/ebe_settings/common.json")
    vars = {
        app_deployment   = local.deployment_name
        app_region       = local.tags.region
        db_password      = random_password.dbadmin.result
        instance_profile = aws_iam_instance_profile.profile.id
        security_group   = aws_security_group.sg.id
        subnet0          = aws_subnet.subnet0.id
        subnet1          = aws_subnet.subnet1.id
        vpc              = aws_vpc.vpc.id
    }
}

data template_file ebe_environment_settings {
    template = file("${path.module}/ebe_settings/${local.tags.environment}.json")
    vars     = {}
}
