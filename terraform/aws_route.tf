resource aws_route internet {
    destination_cidr_block = "0.0.0.0/0"
    gateway_id             = aws_internet_gateway.gw.id
    route_table_id         = aws_route_table.rt.id
}
