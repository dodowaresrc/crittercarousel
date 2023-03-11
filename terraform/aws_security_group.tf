resource aws_security_group sg {

    name        = local.deployment_name
    description = "trusted ssh"
    vpc_id      = aws_vpc.vpc.id

    ingress {
        description      = "trusted ssh"
        from_port        = 22
        to_port          = 22
        protocol         = "tcp"
        cidr_blocks      = var.ssh_config == null ? [] : [for x in var.ssh_config.trusted_hosts: "${x}/32"]
    }

    egress {
        from_port        = 0
        to_port          = 0
        protocol         = "-1"
        cidr_blocks      = ["0.0.0.0/0"]
        ipv6_cidr_blocks = ["::/0"]
    }
}
