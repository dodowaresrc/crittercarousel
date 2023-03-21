resource aws_security_group vm {

    name        = "${local.deployment_name}-vm"
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
    }
}

resource aws_security_group db {
    name        = "${local.deployment_name}-db"
    description = "db access from ec2 instances"
    vpc_id      =  aws_vpc.vpc.id

    ingress {
        from_port = 5432
        to_port = 5432
        protocol = "tcp"
        cidr_blocks = [aws_subnet.subnet0.cidr_block, aws_subnet.subnet1.cidr_block]

    }

    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = [aws_subnet.subnet0.cidr_block, aws_subnet.subnet1.cidr_block]
    }
}
