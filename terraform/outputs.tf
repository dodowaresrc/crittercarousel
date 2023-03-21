output vpc {
    value = aws_vpc.vpc.id
}

output ecr {
    value = aws_ecr_repository.repo.repository_url
}

output lb {
    value = aws_elastic_beanstalk_environment.env.load_balancers[0]
}
