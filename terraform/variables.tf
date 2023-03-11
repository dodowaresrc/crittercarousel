variable base_tags {
    type = object({
        color       = string
        component   = string
        environment = string
        owner       = string
        project     = string
        region      = string
    })
}

variable application_version {
    type = string
}

variable ssh_config {
    type = object({
        public_key_file = string
        trusted_hosts   = list(string)
    })
    default = null
}
