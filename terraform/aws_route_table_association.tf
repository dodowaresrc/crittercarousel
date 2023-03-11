resource aws_route_table_association subnet0 {
    route_table_id = aws_route_table.rt.id
    subnet_id      = aws_subnet.subnet0.id
}

resource aws_route_table_association subnet1 {
    route_table_id = aws_route_table.rt.id
    subnet_id      = aws_subnet.subnet1.id
}