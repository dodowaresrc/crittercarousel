resource aws_elastic_beanstalk_environment env {
    application            = aws_elastic_beanstalk_application.app.name
    name                   = local.deployment_name
    solution_stack_name    = "64bit Amazon Linux 2 v3.5.4 running Docker"
    wait_for_ready_timeout = "60m"

    dynamic setting {
        for_each = local.ebe_settings
        content {
            namespace = setting.value.namespace
            name = setting.value.name
            value = setting.value.value
        }
    }
}
