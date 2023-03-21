resource aws_subnet subnet0 {
    availability_zone       = data.aws_availability_zones.azones.names[0]
    cidr_block              = "192.168.0.0/24"
    map_public_ip_on_launch = true
    tags                    = local.tags
    vpc_id                  = aws_vpc.vpc.id
}

resource aws_subnet subnet1 {
    availability_zone       = data.aws_availability_zones.azones.names[1]
    cidr_block              = "192.168.1.0/24"
    map_public_ip_on_launch = true
    tags                    = local.tags
    vpc_id                  = aws_vpc.vpc.id
}
