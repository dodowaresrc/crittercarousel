[CmdletBinding()]

Param(
    [Parameter(Mandatory=$True)] $Version,
    [Parameter(Mandatory=$True)] $Region,
    [switch] $NoPush
)

 $Image = "crittercarousel-api"

$RegistryInfo = aws ecr describe-registry --region $Region | ConvertFrom-Json

$RegistryHost = "$($RegistryInfo.registryId).dkr.ecr.${Region}.amazonaws.com"

$RepositoryUri = "${RegistryHost}/${Image}"

Write-Host "RepositoryUri=${RepositoryUri}"

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
