locals {

    short_region = replace(var.base_tags.region, "-", "")

    application_name = join("-", [
        var.base_tags.project,
        var.base_tags.component
    ])

    application_name_title = join("", [
        title(var.base_tags.project),
        title(var.base_tags.component)
    ])

    deployment_name = join("-", [
        var.base_tags.project,
        var.base_tags.component,
        local.short_region,
        var.base_tags.color
    ])

    deployment_name_title = join("", [
        title(var.base_tags.project),
        title(var.base_tags.component),
        title(local.short_region),
        title(var.base_tags.color)
    ])

    container_url = format("%s:%s", aws_ecr_repository.repo.repository_url, var.application_version)

    full_name = join("-", [
        var.base_tags.project,
        var.base_tags.component,
        var.base_tags.environment,
        local.short_region,
        var.base_tags.color
    ])

    tags = merge(var.base_tags, {
        full_name=local.full_name,
        short_region=local.short_region,
        deployment_name=local.deployment_name,
        application_name=local.application_name,
    })

    docker_environment_variables = [
        "APP_DEPLOYMENT",
        "APP_REGION",
        "RDS_HOSTNAME",
        "RDS_PORT",
        "RDS_DB_NAME",
        "RDS_USERNAME",
        "RDS_PASSWORD"
    ]

    docker_compose_data = {
        services = {
            application = {
                environment = local.docker_environment_variables
                image       = "${aws_ecr_repository.repo.repository_url}:${var.application_version}"
                ports       = ["8888:8888"]
            }
        }
    }

    ebe_ssh_settings = var.ssh_config == null ? [] : [{
        namespace = "aws:autoscaling:launchconfiguration"
        name      = "EC2KeyName"
        value     = aws_key_pair.keypair[0].id
    }]

    ebe_settings = concat(
        jsondecode(data.template_file.ebe_common_settings.rendered),
        jsondecode(data.template_file.ebe_environment_settings.rendered),
        local.ebe_ssh_settings
    )
}
