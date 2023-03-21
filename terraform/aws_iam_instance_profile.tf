resource aws_iam_instance_profile profile {
    name = local.deployment_name
    role = aws_iam_role.role.id
}
