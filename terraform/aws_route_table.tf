resource aws_route_table rt {
    tags   = local.tags
    vpc_id = aws_vpc.vpc.id
}
