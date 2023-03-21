resource aws_db_subnet_group postgres {
  name       = "postgres"
  subnet_ids = [aws_subnet.subnet0.id, aws_subnet.subnet1.id]

}