resource aws_db_instance postgres {
    allocated_storage      = 5
    availability_zone      = "us-east-1a"
    db_name                = local.deployment_name_title
    db_subnet_group_name   = aws_db_subnet_group.postgres.name
    engine                 = "postgres"
    engine_version         = "14.7"
    instance_class         = "db.t3.micro"
    username               = "dbadmin"
    password               = random_password.dbadmin.result
    skip_final_snapshot    = true
    vpc_security_group_ids = [aws_security_group.db.id]
}
