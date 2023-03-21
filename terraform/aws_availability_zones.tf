data aws_availability_zones azones {
    
    state = "available"

    filter {
        name   = "group-name"
        values = [var.base_tags.region]
    }
}
