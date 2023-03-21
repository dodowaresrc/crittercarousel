function Build-CritterContainer
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)] $BaseTags,
        [Parameter(Mandatory=$True)] $Version,
        [switch] $NoPush
    )

    $ErrorActionPreference = "Stop"

    $RegistryInfo = aws ecr describe-registry --region $Region | ConvertFrom-Json

    $RegistryHost = "$($RegistryInfo.registryId).dkr.ecr.${Region}.amazonaws.com"

    $RepositoryUri = "${RegistryHost}/${Image}"

    docker build . `
        -t "${Image}:latest" `
        -t "${Image}:${Version}" `
        -t "${RepositoryUri}:latest" `
        -t "${RepositoryUri}:${Version}"

    aws ecr get-login-password --region $Region | docker login --username AWS --password-stdin $RegistryHost

    if (-not $NoPush) {
        docker push "${RepositoryUri}:${Version}"
        docker push "${RepositoryUri}:latest"
    }
}
