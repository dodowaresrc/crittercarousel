resource aws_key_pair keypair {
    count      = var.ssh_config == null ? 0 : 1
    key_name   = local.deployment_name
    public_key = file(var.ssh_config.public_key_file)
}
